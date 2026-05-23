document.addEventListener('DOMContentLoaded', () => {
    const langToggleBtn = document.getElementById('lang-toggle');
    let currentLang = 'en';

    // 1. DUAL LANGUAGE SWITCHER LOGIC
    langToggleBtn.addEventListener('click', () => {
        if (currentLang === 'en') {
            // Hide English, Show Spanish
            document.querySelectorAll('.lang-en').forEach(el => el.classList.add('hidden'));
            document.querySelectorAll('.lang-es').forEach(el => el.classList.remove('hidden'));
            currentLang = 'es';
        } else {
            // Hide Spanish, Show English
            document.querySelectorAll('.lang-es').forEach(el => el.classList.add('hidden'));
            document.querySelectorAll('.lang-en').forEach(el => el.classList.remove('hidden'));
            currentLang = 'en';
        }
    });

    // 2. FUTURE SCALE EXPANSION OPTION
    // This function showcases how easily you can hook up a cloud database (like MongoDB Atlas or an API) to add images later.
    const addWorkBtn = document.getElementById('add-work-trigger');
    const galleryGrid = document.getElementById('portfolio-gallery');

    addWorkBtn.addEventListener('click', () => {
        // Mocking an upload or fetch event for new showcase items
        const newImages = [
            'https://images.unsplash.com/photo-1507136566006-cfc505b114fc?w=600', // Waxing job
            'https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?w=600'  // Clean Sports Sedan Finish
        ];

        newImages.forEach(url => {
            const item = document.createElement('div');
            item.className = 'gallery-item';
            item.innerHTML = `<img src="${url}" alt="New Detail Work Showcase">`;
            galleryGrid.appendChild(item);
        });

        // Flash alert feedback
        alert(currentLang === 'en' ? 'New portfolio placeholders loaded successfully!' : '¡Nuevas muestras de portafolio cargadas con éxito!');
    });
});