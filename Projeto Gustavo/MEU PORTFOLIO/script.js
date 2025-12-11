// script.js — tema, scroll suave, menu, carrossel, modal, tilt, formulário

// ======================
// ELEMENTOS PRINCIPAIS
// ======================
const htmlEl      = document.documentElement;
const themeSelect = document.getElementById('theme-select');
const smoothBtn   = document.getElementById('smooth-toggle');
const menuBtn     = document.getElementById('menu-toggle');
const mainNav     = document.getElementById('main-nav');

// ======================
// TEMA
// ======================
htmlEl.dataset.theme = 'white';

themeSelect.addEventListener('change', e => {
  htmlEl.dataset.theme = e.target.value;
});

// ======================
// SCROLL SUAVE
// ======================
let smoothEnabled = true;

smoothBtn.addEventListener('click', () => {
  smoothEnabled = !smoothEnabled;
  htmlEl.style.scrollBehavior = smoothEnabled ? 'smooth' : 'auto';
  smoothBtn.textContent = `Scroll suave: ${smoothEnabled ? 'ON' : 'OFF'}`;
});

// ======================
// MENU MOBILE
// ======================
menuBtn.addEventListener('click', () => {
  const open = menuBtn.getAttribute('aria-expanded') === 'true';
  menuBtn.setAttribute('aria-expanded', !open);
  mainNav.style.display = open ? 'none' : 'flex';
});

// ======================
// CARROSSEL
// ======================
const slides     = document.querySelector('.carrossel-pro .slides');
const slideImgs  = document.querySelectorAll('.carrossel-pro .slides img');
const nextBtns   = document.querySelectorAll('.carrossel-pro .next');
const prevBtns   = document.querySelectorAll('.carrossel-pro .prev');
let cIndex       = 0;

const updateSlides = () => {
  slides.style.transform = `translateX(${-cIndex * 100}%)`;
};

// botões
nextBtns.forEach(btn => btn.addEventListener('click', () => {
  cIndex = (cIndex + 1) % slideImgs.length;
  updateSlides();
}));

prevBtns.forEach(btn => btn.addEventListener('click', () => {
  cIndex = (cIndex - 1 + slideImgs.length) % slideImgs.length;
  updateSlides();
}));

// autoplay
let autoPlay = setInterval(() => {
  cIndex = (cIndex + 1) % slideImgs.length;
  updateSlides();
}, 3500);

slides.addEventListener('mouseenter', () => clearInterval(autoPlay));
slides.addEventListener('mouseleave', () => {
  autoPlay = setInterval(() => {
    cIndex = (cIndex + 1) % slideImgs.length;
    updateSlides();
  }, 3500);
});

// ======================
// MODAL DE PROJETOS
// ======================
const cards      = document.querySelectorAll('.project-card');
const modal      = document.getElementById('modal');
const modalImg   = document.getElementById('modal-img');
const modalDesc  = document.getElementById('modal-desc');
const modalClose = document.getElementById('modal-close');

const openModal = card => {
  const img   = card.dataset.img || card.querySelector('img')?.src;
  const title = card.querySelector('h3')?.textContent || '';
  const text  = card.querySelector('p')?.textContent || '';

  modalImg.src = img;
  modalDesc.innerHTML = `<h3>${title}</h3><p>${text}</p>`;
  modal.setAttribute('aria-hidden', 'false');
  document.body.style.overflow = 'hidden';
};

const closeModal = () => {
  modal.setAttribute('aria-hidden', 'true');
  document.body.style.overflow = '';
};

cards.forEach(card => {
  card.addEventListener('click', () => openModal(card));
  card.addEventListener('keydown', e => {
    if (e.key === 'Enter') openModal(card);
  });
});

modalClose.addEventListener('click', closeModal);
modal.addEventListener('click', e => {
  if (e.target === modal) closeModal();
});

document.addEventListener('keydown', e => {
  if (e.key === 'Escape' && modal.getAttribute('aria-hidden') === 'false') {
    closeModal();
  }
});

// ======================
// EFEITO TILT
// ======================
document.querySelectorAll('[data-tilt]').forEach(el => {
  el.addEventListener('mousemove', ev => {
    const rect = el.getBoundingClientRect();
    const x = ev.clientX - rect.left;
    const y = ev.clientY - rect.top;

    const rotY = (x / rect.width - 0.5) * 12;
    const rotX = (y / rect.height - 0.5) * -8;

    el.style.transform = `
      perspective(600px)
      rotateX(${rotX}deg)
      rotateY(${rotY}deg)
      translateZ(6px)
    `;
  });

  el.addEventListener('mouseleave', () => {
    el.style.transform = '';
  });
});

// ======================
// FORMULÁRIO DE CONTATO
// ======================
const form = document.getElementById('contact-form');

form.addEventListener('submit', e => {
  e.preventDefault();
  alert('Formulário enviado (simulação). Obrigado — vou responder por email quando possível.');
  form.reset();
});
