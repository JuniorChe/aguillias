document.addEventListener('DOMContentLoaded', () => {
    const langToggleBtn = document.getElementById('lang-toggle');
    let currentLang = 'en';

    langToggleBtn.addEventListener('click', () => {
        if (currentLang === 'en') {
            document.querySelectorAll('.lang-en').forEach(el => el.classList.add('hidden'));
            document.querySelectorAll('.lang-es').forEach(el => el.classList.remove('hidden'));
            currentLang = 'es';
        } else {
            document.querySelectorAll('.lang-es').forEach(el => el.classList.add('hidden'));
            document.querySelectorAll('.lang-en').forEach(el => el.classList.remove('hidden'));
            currentLang = 'en';
        }
    });
});