const grid = 21;

const SPEED = {
  easy: 180,
  medium: 90,
  hard: 60
};

const modeScreen = document.getElementById("modeScreen");
const configScreen = document.getElementById("configScreen");
const gameScreen = document.getElementById("gameScreen");
const resultScreen = document.getElementById("resultScreen");

const p1Input = document.getElementById("p1Name");
const p2Input = document.getElementById("p2Name");
const diffSel = document.getElementById("difficulty");
const timeSel = document.getElementById("timeSelect");

const label1 = document.getElementById("label1");
const label2 = document.getElementById("label2");
const timerEl = document.getElementById("timer");
const resultText = document.getElementById("resultText");
const bestScoreText = document.getElementById("bestScoreText");

const rankingList = document.getElementById("rankingList");

let mode = "";

// =======================
// RANKING (TOP 3)
// =======================
function getRanking() {
  return JSON.parse(localStorage.getItem("snakeRanking")) || [];
}

function saveRanking(ranking) {
  localStorage.setItem("snakeRanking", JSON.stringify(ranking));
}

function updateRanking(name, score) {
  let ranking = getRanking();
  ranking.push({ name, score });
  ranking.sort((a, b) => b.score - a.score);
  ranking = ranking.slice(0, 3);
  saveRanking(ranking);
}

function renderRanking() {
  rankingList.innerHTML = "";
  getRanking().forEach(p => {
    const li = document.createElement("li");
    li.textContent = `${p.name} - ${p.score}`;
    rankingList.appendChild(li);
  });
}

// =======================
// MODO
// =======================
soloBtn.onclick = () => openConfig("solo");
battleBtn.onclick = () => openConfig("battle");

function openConfig(m) {
  mode = m;
  modeScreen.classList.remove("active");
  configScreen.classList.add("active");

  document.getElementById("configTitle").textContent =
    m === "solo" ? "1 Jogador" : "Modo Batalha";

  p2Input.style.display = m === "battle" ? "block" : "none";
  timeSel.style.display = m === "battle" ? "block" : "none";
}

// =======================
// INICIAR
// =======================
startGame.onclick = () => {
  configScreen.classList.remove("active");
  gameScreen.classList.add("active");

  const speed = SPEED[diffSel.value];

  label1.textContent = p1Input.value || "Jogador 1";
  label2.textContent = p2Input.value || "Jogador 2";

  const p1 = createPlayer("game1", "score1", {
    up: "ArrowUp", down: "ArrowDown", left: "ArrowLeft", right: "ArrowRight"
  }, speed, label1.textContent);

  let p2;
  if (mode === "battle") {
    document.getElementById("player2Box").style.display = "block";
    p2 = createPlayer("game2", "score2", {
      up: "w", down: "s", left: "a", right: "d"
    }, speed, label2.textContent);

    renderRanking();
    startTimer(p1, p2);
  } else {
    document.getElementById("player2Box").style.display = "none";
    document.getElementById("timerBox").style.display = "none";
  }
};

// =======================
// TIMER BATALHA
// =======================
function startTimer(p1, p2) {
  let time = Number(timeSel.value);
  timerEl.textContent = time;

  const timer = setInterval(() => {
    time--;
    timerEl.textContent = time;

    if (time <= 0) {
      clearInterval(timer);
      endBattle(p1, p2); // 👈 AGORA CHAMA O FINAL CORRETO
    }
  }, 1000);
}

// =======================
// PLAYER
// =======================
function createPlayer(canvasId, scoreId, controls, speed, name) {
  const canvas = document.getElementById(canvasId);
  const ctx = canvas.getContext("2d");
  const scoreEl = document.getElementById(scoreId);

  let snake = [{ x: 210, y: 210 }];
  let food = spawnFood();

  let dx = 0;
  let dy = 0;

  let score = 0;
  let alive = true;
  let started = false; // 👈 CONTROLA SE O JOGO JÁ COMEÇOU

  function spawnFood() {
    return {
      x: Math.floor(Math.random() * 20) * grid,
      y: Math.floor(Math.random() * 20) * grid
    };
  }

  function tick() {
    if (!alive) return;

    draw();

    // 🚫 NÃO SE MOVE NEM MORRE ANTES DE COMEÇAR
    if (!started) return;

    const nx = snake[0].x + dx;
    const ny = snake[0].y + dy;

    // ☠️ MORTE OBRIGATÓRIA NA PAREDE
    if (
      nx < 0 || ny < 0 ||
      nx >= canvas.width || ny >= canvas.height
    ) {
      alive = false;
      endSolo();
      return;
    }

    const head = { x: nx, y: ny };

    // ☠️ MORTE AO BATER NO PRÓPRIO CORPO
    if (snake.some(p => p.x === head.x && p.y === head.y)) {
      alive = false;
      endSolo();
      return;
    }

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
    ctx.beginPath();
    ctx.arc(food.x + grid / 2, food.y + grid / 2, grid / 2 - 2, 0, Math.PI * 2);
    ctx.fill();

    // cobra
    snake.forEach((p, i) => {
      ctx.fillStyle = i === 0 ? "#22c55e" : "#16a34a";
      ctx.beginPath();
      ctx.arc(p.x + grid / 2, p.y + grid / 2, grid / 2 - 1, 0, Math.PI * 2);
      ctx.fill();
    });
  }

  function endSolo() {
    if (mode !== "solo") return;

    const best = Math.max(
      score,
      Number(localStorage.getItem("bestScore") || 0)
    );

    localStorage.setItem("bestScore", best);
    updateRanking(name, score);

    resultText.textContent = "Você morreu!";
    bestScoreText.textContent = `Pontuação: ${score} | Melhor: ${best}`;

    gameScreen.classList.remove("active");
    resultScreen.classList.add("active");
  }

  // 🎮 CONTROLES (FUNCIONA PARA 1 E 2 JOGADORES)
  document.addEventListener("keydown", e => {
    if (!alive) return;

    if (e.key === controls.up && dy === 0) {
      dx = 0;
      dy = -grid;
      started = true;
    }

    if (e.key === controls.down && dy === 0) {
      dx = 0;
      dy = grid;
      started = true;
    }

    if (e.key === controls.left && dx === 0) {
      dx = -grid;
      dy = 0;
      started = true;
    }

    if (e.key === controls.right && dx === 0) {
      dx = grid;
      dy = 0;
      started = true;
    }
  });

  const loop = setInterval(tick, speed);

  return {
    name,
    getScore: () => score,
    stop: () => clearInterval(loop)
  };
}



function endBattle(p1, p2) {
  // Para os dois jogos
  p1.stop();
  p2.stop();

  // Atualiza ranking global
  updateRanking(p1.name, p1.getScore());
  updateRanking(p2.name, p2.getScore());

  // Decide vencedor
  let message = "";

  if (p1.getScore() > p2.getScore()) {
    message = `🏆 ${p1.name} venceu!`;
  } else if (p2.getScore() > p1.getScore()) {
    message = `🏆 ${p2.name} venceu!`;
  } else {
    message = "🤝 Empate!";
  }

  // Atualiza texto
  resultText.textContent = message;
  bestScoreText.textContent = 
    `${p1.name}: ${p1.getScore()} pontos | ${p2.name}: ${p2.getScore()} pontos`;

  // Troca de tela
  gameScreen.classList.remove("active");
  resultScreen.classList.add("active");
}
