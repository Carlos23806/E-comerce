document.addEventListener('DOMContentLoaded', () => {
    const nav = document.querySelector('.nav');
    const currentPath = window.location.pathname;
    
    if (currentPath === '/' || currentPath === '/home/') {
        nav.classList.add('nav-home');
        
        window.addEventListener('scroll', () => {
            if (window.scrollY > 20) {
                nav.classList.remove('nav-home');
                nav.classList.add('nav-scrolled');
            } else {
                nav.classList.add('nav-home');
                nav.classList.remove('nav-scrolled');
            }
        });
    } else if (currentPath === '/addproduct/'){
        nav.classList.add('nav-register');
    } else {
        nav.classList.add('nav-scrolled');
    }
});