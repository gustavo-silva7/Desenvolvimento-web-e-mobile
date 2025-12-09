const slides = document.querySelector('.slides');
const images = document.querySelectorAll('.slides img');
let index = 0;

document.querySelector('.next').addEventListener('click', () => {
    index++;
    if (index > images.length - 1) index = 0;
    updateCarousel();
});

document.querySelector('.prev').addEventListener('click', () => {
    index--;
    if (index < 0) index = images.length - 1;
    updateCarousel();
});

function updateCarousel() {
    slides.style.transform = `translateX(${-index * 100}%)`;
}

