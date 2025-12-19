const grid = 21;

// Velocidades (fácil = base)
const SPEED = {
  easy: 180,
  medium: 90,
  hard: 60
};

// Telas
const modeScreen = document.getElementById("modeScreen");
const configScreen = document.getElementById("configScreen");
const gameScreen = document.getElementById("gameScreen");
const resultScreen = document.getElementById("resultScreen");

// Inputs
const wallDeath = document.getElementById("wallDeath");
const diffSel = document.getElementById("difficulty");
const timeSel = document.getElementById("timeSelect");
const p1Input = document.getElementById("p1Name");
const p2Input = document.getElementById("p2Name");

// Labels
const label1 = document.getElementById("label1");
const label2 = document.getElementById("label2");
const timerEl = document.getElementById("timer");
const resultText = document.getElementById("resultText");

let mode = "";

// Botões
soloBtn.onclick = () => openConfig("solo");
battleBtn.onclick = () => openConfig("battle");

function openConfig(m) {
  mode = m;
  modeScreen.classList.remove("active");
  configScreen.classList.add("active");

  document.getElementById("configTitle").textContent =
    mode === "solo" ? "1 Jogador" : "Modo Batalha";

  p2Input.style.display = mode === "battle" ? "block" : "none";
  timeSel.style.display = mode === "battle" ? "block" : "none";
}

// Iniciar jogo
startGame.onclick = () => {
  configScreen.classList.remove("active");
  gameScreen.classList.add("active");

  label1.textContent = p1Input.value || "Jogador 1";
  label2.textContent = p2Input.value || "Jogador 2";

  const speed = SPEED[diffSel.value];
  const dieOnWall = wallDeath.checked;

  const p1 = createPlayer("game1", "score1", {
    up: "ArrowUp", down: "ArrowDown", left: "ArrowLeft", right: "ArrowRight"
  }, speed, dieOnWall);

  let p2;
  if (mode === "battle") {
    document.getElementById("player2Box").style.display = "block";
    p2 = createPlayer("game2", "score2", {
      up: "w", down: "s", left: "a", right: "d"
    }, speed, dieOnWall);

    startTimer(p1, p2);
  } else {
    document.getElementById("player2Box").style.display = "none";
    document.getElementById("timerBox").style.display = "none";
  }
};

// Timer do modo batalha
function startTimer(p1, p2) {
  let time = Number(timeSel.value);
  timerEl.textContent = time;

  const t = setInterval(() => {
    time--;
    timerEl.textContent = time;

    if (time <= 0) {
      clearInterval(t);
      p1.stop();
      p2.stop();
      endBattle(p1, p2);
    }
  }, 1000);
}

function endBattle(p1, p2) {
  gameScreen.classList.remove("active");
  resultScreen.classList.add("active");

  resultText.textContent =
    p1.getScore() > p2.getScore() ? `${label1.textContent} venceu!` :
    p2.getScore() > p1.getScore() ? `${label2.textContent} venceu!` :
    "Empate!";
}

// =================
// PLAYER / SNAKE
// =================
function createPlayer(canvasId, scoreId, controls, speed, dieOnWall) {
  const canvas = document.getElementById(canvasId);
  const ctx = canvas.getContext("2d");
  const scoreEl = document.getElementById(scoreId);

  let snake = [{ x: 210, y: 210 }];
  let food = spawnFood();
  let dx = 0, dy = 0;
  let score = 0;
  let started = false;

  function spawnFood() {
    return {
      x: Math.floor(Math.random() * 20) * grid,
      y: Math.floor(Math.random() * 20) * grid
    };
  }

  function tick() {
    draw();
    if (!started) return;

    let nx = snake[0].x + dx;
    let ny = snake[0].y + dy;

    // Parede
    if (dieOnWall && (nx < 0 || ny < 0 || nx >= canvas.width || ny >= canvas.height)) {
      clearInterval(loop);
      return;
    }

    // Teleporte se não morrer
    nx = (nx + canvas.width) % canvas.width;
    ny = (ny + canvas.height) % canvas.height;

    const head = { x: nx, y: ny };

    if (snake.some(p => p.x === head.x && p.y === head.y)) return;

    snake.unshift(head);

    if (head.x === food.x && head.y === food.y) {
      score++;
      scoreEl.textContent = score;
      food = spawnFood();
    } else {
      snake.pop();
    }
  }

  function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // comida
    ctx.fillStyle = "#ef4444";
    ctx.shadowBlur = 15;
    ctx.shadowColor = "#ef4444";
    ctx.beginPath();
    ctx.arc(food.x + grid/2, food.y + grid/2, grid/2 - 2, 0, Math.PI*2);
    ctx.fill();

    // cobra
    snake.forEach((p, i) => {
      ctx.fillStyle = i === 0 ? "#22c55e" : "#16a34a";
      ctx.shadowBlur = 10;
      ctx.shadowColor = "#22c55e";
      ctx.beginPath();
      ctx.arc(p.x + grid/2, p.y + grid/2, grid/2 - 1, 0, Math.PI*2);
      ctx.fill();
    });

    ctx.shadowBlur = 0;
  }

  document.addEventListener("keydown", e => {
    if (!started) started = true;

    if (e.key === controls.up && dy === 0) [dx, dy] = [0, -grid];
    if (e.key === controls.down && dy === 0) [dx, dy] = [0, grid];
    if (e.key === controls.left && dx === 0) [dx, dy] = [-grid, 0];
    if (e.key === controls.right && dx === 0) [dx, dy] = [grid, 0];
  });

  const loop = setInterval(tick, speed);

  return {
    getScore: () => score,
    stop: () => clearInterval(loop)
  };
}
