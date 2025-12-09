// Alternar tema claro/escuro
const root = document.body;
const savedTheme = localStorage.getItem("site-theme");
if (savedTheme === "dark") root.classList.add("theme-dark");

document.getElementById("themeToggle").addEventListener("click", () => {
  root.classList.toggle("theme-dark");
  const dark = root.classList.contains("theme-dark");
  localStorage.setItem("site-theme", dark ? "dark" : "light");
});

// Mostrar / Esconder alunos
const alunosBtn = document.getElementById("toggleAlunos");
const alunosGrid = document.getElementById("alunosGrid");

alunosBtn.addEventListener("click", () => {
  alunosGrid.classList.toggle("hidden");
  alunosBtn.textContent = alunosGrid.classList.contains("hidden")
    ? "Mostrar Alunos"
    : "Esconder Alunos";
});

// Rolagem suave
document.querySelectorAll(".nav-link, [data-target]").forEach(link => {
  link.addEventListener("click", (e) => {
    e.preventDefault();
    const target = link.getAttribute("href") || link.getAttribute("data-target");
    const el = document.querySelector(target);
    if (el) el.scrollIntoView({ behavior: "smooth" });
  });
});

// Confirmação do formulário
document.getElementById("contactForm").addEventListener("submit", (e) => {
  e.preventDefault();
  const nome = document.getElementById("nome").value;
  alert(`Obrigado, ${nome}! Sua mensagem foi enviada.`);
  e.target.reset();
});
