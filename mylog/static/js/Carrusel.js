document.addEventListener('DOMContentLoaded', function() {
    const heroBackground = document.querySelector('.hero-carousel-background');
    const indicators = document.querySelectorAll('.indicator');
    const images = document.querySelectorAll('[data-carousel-image]');
    
    if (!images.length) {
        console.error('No se encontraron imágenes para el carrusel');
        return;
    }

    const backgroundImages = Array.from(images).map(img => img.getAttribute('data-carousel-image'));
    let currentImageIndex = 0;
    let isTransitioning = false;

    function preloadImages() {
        return Promise.all(backgroundImages.map(src => {
            return new Promise((resolve, reject) => {
                const img = new Image();
                img.onload = () => {
                    console.log('Imagen cargada:', src);
                    resolve(src);
                };
                img.onerror = () => {
                    console.error('Error cargando imagen:', src);
                    reject(`Error loading image: ${src}`);
                };
                img.src = src;
            });
        }));
    }

    function changeBackground() {
        if (isTransitioning) return;
        isTransitioning = true;

        console.log('Cambiando a imagen:', backgroundImages[currentImageIndex]);
        heroBackground.style.opacity = '0';
        
        setTimeout(() => {
            heroBackground.style.backgroundImage = `url("${backgroundImages[currentImageIndex]}")`;
            heroBackground.style.opacity = '1';
            updateIndicators();
            currentImageIndex = (currentImageIndex + 1) % backgroundImages.length;
            isTransitioning = false;
        }, 1000);
    }

    function updateIndicators() {
        indicators.forEach((indicator, index) => {
            indicator.classList.toggle('active', index === currentImageIndex);
        });
    }

    // Inicialización con más logging
    console.log('Iniciando carrusel...');
    console.log('Imágenes encontradas:', backgroundImages);
    
    preloadImages()
        .then(() => {
            console.log('Imágenes precargadas exitosamente');
            heroBackground.style.backgroundImage = `url("${backgroundImages[0]}")`;
            updateIndicators();
            setInterval(changeBackground, 5000);
        })
        .catch(error => {
            console.error('Error en la precarga:', error);
            heroBackground.style.backgroundColor = '#333';
        });
});