const cards = document.querySelectorAll('.card');

function showCardsOnScroll() {
    cards.forEach(card => {
        const cardTop = card.getBoundingClientRect().top;
        const screenHeight = window.innerHeight * 0.8;

        if (cardTop < screenHeight) {
            card.classList.add('show');
        }
    });
}

window.addEventListener('scroll', showCardsOnScroll);
showCardsOnScroll();
