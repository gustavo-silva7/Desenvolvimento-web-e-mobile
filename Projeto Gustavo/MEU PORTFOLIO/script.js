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
// document.addEventListener('DOMContentLoaded', () => {
//     const slides = document.querySelector('.interativo-carro .slides-carro');
//     const imagemslides = document.querySelectorAll('.interativo-carro .slides-carro img');
//     const proximobnt = document.querySelector('.interativo-carro .proximo');
//     const anteriorbnt = document.querySelector('.interativo-carro .anterior');

//     let cIndex = 0;

//     const updateSlides = () => {
//     slides.style.transform = `translateX(-${cIndex * 100}%)`;
//     };

//     // PRÓXIMO (limitado)
//     proximobnt.forEach(button => {
//     button.addEventListener('click', () => {
//         if (cIndex < imagemslides.length - 1) {
//         cIndex++;
//         updateSlides();
//         }
//     });
//     });

//     // ANTERIOR (loopa corretamente)
//     anteriorbnt.forEach(button => {
//     button.addEventListener('click', () => {
//         if (cIndex === 0) {
//             cIndex = imagemslides.length - 1;
//         } else {
//             cIndex--;
//         }
//         updateSlides();
//     });
//     });

//     // AUTO SLIDE
//     let autoSlideInterval = setInterval(() => {
//         cIndex = (cIndex + 1) % imagemslides.length;
//         updateSlides();
//     }, 4000);

//     slides.addEventListener('mouseenter', () => {
//         clearInterval(autoSlideInterval);
//     });

//     slides.addEventListener('mouseleave', () => {
//         autoSlideInterval = setInterval(() => {
//             cIndex = (cIndex + 1) % imagemslides.length;
//             updateSlides();
//     }, 4000);
//     });
// });

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
   }, 4000);

   slides.addEventListener('mouseenter', () => {
     clearInterval(autoSlideInterval);
   });

   slides.addEventListener('mouseleave', () => {
     autoSlideInterval = setInterval(() => {
       cIndex = (cIndex + 1) % imagemslides.length;
       updateSlides();
     }, 4000);
   });
});

