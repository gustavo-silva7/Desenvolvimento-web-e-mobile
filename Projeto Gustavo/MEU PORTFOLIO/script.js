const botao = document.getElementById("seleciona-tema")
// const icon = document.getElementById("icons")

botao.addEventListener("click", () => {
    const atual = document.documentElement.getAttribute("data-theme");
    const novo = atual === "escuro" ? "claro" : "escuro";
    document.documentElement.setAttribute("data-theme", novo);
    localStorage.setItem("tema", novo);
    // document.body.classList.toggle("escuro");
    // const escuro = document.body.classList.contains("escuro")
    // // icon.src = escuro ? "imagens/sol.ico" : "imagens/lua.svg";
    // localStorage.setItem("temas", escuro? "escuro" : "claro");
});

//APLICA TEMA SALVO
const salvo = localStorage.getItem("tema")
// if (saved === "escuro"){
//     document.body.classList.add("escuro");}
if (salvo) {
document.documentElement.setAttribute("data-theme", salvo);
}

// // //CARROSSEL
document.addEventListener('DOMContentLoaded', () => {
  const slides = document.querySelector('.interativo-carro .slides-carro');
  const imagemslides = document.querySelectorAll('.interativo-carro .slides-carro img');
  const proximobnt = document.querySelector('.interativo-carro .proximo');
  const anteriorbnt = document.querySelector('.interativo-carro .anterior');

  let cIndex = 0;

  const updateSlides = () => {
    slides.style.transform = `translateX(-${cIndex * 100}%)`;
  };

  // PRÓXIMO
  proximobnt.addEventListener('click', () => {
    cIndex = (cIndex - 1) % imagemslides.length;
    updateSlides();
  });

  // ANTERIOR
  anteriorbnt.addEventListener('click', () => {
    cIndex = (cIndex + 1 + imagemslides.length) % imagemslides.length;
    updateSlides();
  });

   // AUTO SLIDE
   let autoSlideInterval = setInterval(() => {
     cIndex = (cIndex + 1) % imagemslides.length;
     updateSlides();
   }, 6000);

   slides.addEventListener('mouseenter', () => {
     clearInterval(autoSlideInterval);
   });

   slides.addEventListener('mouseleave', () => {
     autoSlideInterval = setInterval(() => {
       cIndex = (cIndex + 1) % imagemslides.length;
       updateSlides();
     }, 6000);
   });
});

// ======================
// CONTATO – EMAILJS
// ======================
// inicializa o EmailJS

(function () {
  emailjs.init("CkvGeXW-STwqN7XC1");
})();

const form = document.getElementById("contato-form");
console.log(form);


form.addEventListener("submit", function (e) {
  e.preventDefault();

  emailjs.sendForm(
    "service_gqby24l",
    "template_kkiotcm",
    this
  )
  .then(() => {
    alert("Obrigado por sua mensagem, vou responder em breve");
    form.reset();
  })
  .catch(error => {
    console.error("Erro:", error);
    alert("Erro ao enviar mensagem. Tente novamente.");
  });
});

//====================
//ABRIR OS PROJETOS 
//====================
function jogar() {
    window.location.href = "Projetos/jogoHTML/index.html";
}

function calcular() {
  alert(
    "Este projeto foi desenvolvido em Python com Tkinter.\n\n" +
    "Para executar:\n" +
    "1️⃣ Baixe o projeto no GitHub\n" +
    "2️⃣ Execute o arquivo calculadora.py com Python instalado"
  );
}
