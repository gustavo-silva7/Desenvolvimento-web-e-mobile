// script.js - interações: tema, smooth scroll, carrossel, modal e efeitos
// Seleciona elementos que usaremos
const themeSelect = document.getElementById('theme-select');
const smoothToggle = document.getElementById('smooth-toggle');
const htmlEl = document.documentElement; // para aplicar data-theme
const menuBtn = document.getElementById('menu-toggle');
const mainNav = document.getElementById('main-nav');

// Aplica tema inicial (minimal)
htmlEl.setAttribute('data-theme','minimal');

// Quando o usuário muda o tema, atualizamos o atributo data-theme
themeSelect.addEventListener('change', (e) => {
  const theme = e.target.value;
  htmlEl.setAttribute('data-theme', theme);
});

// Controle de scroll suave: ativa/desativa comportamento de rolagem
let smoothEnabled = true;
smoothToggle.addEventListener('click', () => {
  smoothEnabled = !smoothEnabled;
  document.documentElement.style.scrollBehavior = smoothEnabled ? 'smooth' : 'auto';
  smoothToggle.textContent = 'Scroll suave: ' + (smoothEnabled ? 'ON' : 'OFF');
});

// Mobile menu toggle (simples)
menuBtn.addEventListener('click', () => {
  const expanded = menuBtn.getAttribute('aria-expanded') === 'true';
  menuBtn.setAttribute('aria-expanded', String(!expanded));
  mainNav.style.display = expanded ? 'none' : 'flex';
});

// CARROSSEL - básico com botões e autoplay
const slides = document.querySelector('.carrossel-pro .slides');
const slideImgs = document.querySelectorAll('.carrossel-pro .slides img');
let cIndex = 0;

function updateSlides(){
  slides.style.transform = `translateX(${-cIndex * 100}%)`;
}

document.querySelectorAll('.carrossel-pro .next').forEach(btn=>{
  btn.addEventListener('click', () => { cIndex = (cIndex +1) % slideImgs.length; updateSlides(); });
});
document.querySelectorAll('.carrossel-pro .prev').forEach(btn=>{
  btn.addEventListener('click', () => { cIndex = (cIndex -1 + slideImgs.length) % slideImgs.length; updateSlides(); });
});

// autoplay suave (pausa ao focar)
let auto = setInterval(()=>{ cIndex = (cIndex +1) % slideImgs.length; updateSlides(); }, 3500);
slides.addEventListener('mouseenter', ()=> clearInterval(auto));
slides.addEventListener('mouseleave', ()=> { auto = setInterval(()=>{ cIndex = (cIndex +1) % slideImgs.length; updateSlides(); }, 3500); });

// PROJECT MODAL - abre detalhes ao clicar em um card
const projectCards = document.querySelectorAll('.project-card');
const modal = document.getElementById('modal');
const modalImg = document.getElementById('modal-img');
const modalDesc = document.getElementById('modal-desc');
const modalClose = document.getElementById('modal-close');

projectCards.forEach(card => {
  card.addEventListener('click', () => {
    const img = card.dataset.img || card.querySelector('img').src;
    const title = card.querySelector('h3').textContent;
    const text = card.querySelector('p').textContent;
    modalImg.src = img;
    modalDesc.innerHTML = `<h3>${title}</h3><p>${text}</p>`;
    modal.setAttribute('aria-hidden','false');
    // Lock scroll while modal aberto
    document.body.style.overflow = 'hidden';
  });

  // also support keyboard open via Enter
  card.addEventListener('keydown', (e) => {
    if(e.key === 'Enter') card.click();
  });
});

// fechar modal
modalClose.addEventListener('click', closeModal);
modal.addEventListener('click', (e) => { if(e.target === modal) closeModal(); });

function closeModal(){
  modal.setAttribute('aria-hidden','true');
  document.body.style.overflow = '';
}

// TILT effect simples: aplica transform conforme mouse move em elementos com [data-tilt]
document.querySelectorAll('[data-tilt]').forEach(el=>{
  el.addEventListener('mousemove', (ev)=>{
    const rect = el.getBoundingClientRect();
    const x = ev.clientX - rect.left;
    const y = ev.clientY - rect.top;
    const px = (x / rect.width - 0.5) * 12; // intensidade
    const py = (y / rect.height - 0.5) * -8;
    el.style.transform = `perspective(600px) rotateX(${py}deg) rotateY(${px}deg) translateZ(6px)`;
  });
  el.addEventListener('mouseleave', ()=> el.style.transform = '');
});

// CONTACT FORM - apenas simula envio e mostra feedback
const form = document.getElementById('contact-form');
form.addEventListener('submit', (e) => {
  e.preventDefault();
  alert('Formulário enviado (simulação). Obrigado — vou responder por email quando possível.');
  form.reset();
});

// Acessibilidade: fechar modal com Escape
document.addEventListener('keydown', (e) => {
  if(e.key === 'Escape' && modal.getAttribute('aria-hidden') === 'false') closeModal();
});
