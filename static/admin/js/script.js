let currentIndex = 0;

function updateCarousel() {
    const carouselInner = document.getElementById('carousel-inner');
    const items = carouselInner.children;
    const totalItems = items.length;

    // Ensure there are items in the carousel
    if (totalItems === 0) return;

    // Move the carousel
    carouselInner.style.transform = `translateX(-${currentIndex * 100}%)`;
}

function moveSlide(step) {
    const carouselInner = document.getElementById('carousel-inner');
    const totalItems = carouselInner.children.length;

    // Ensure there are items to slide
    if (totalItems === 0) return;

    currentIndex = (currentIndex + step + totalItems) % totalItems;
    updateCarousel();
}

// Initialize the carousel
document.addEventListener('DOMContentLoaded', () => {
    updateCarousel();
});
