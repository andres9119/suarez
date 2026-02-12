document.addEventListener('DOMContentLoaded', function () {

    // Navbar background on scroll
    const navbar = document.querySelector('.navbar-custom');
    if (navbar) {
        window.addEventListener('scroll', function () {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        }, { passive: true });
    }

    // Animate elements on scroll
    const observer = new IntersectionObserver(function (entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-fade-in');
            }
        });
    }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

    document.querySelectorAll('.animate-fade').forEach(el => observer.observe(el));

    // Initialize Bootstrap tooltips lazily
    if (typeof bootstrap !== 'undefined') {
        const tooltips = document.querySelectorAll('[data-bs-toggle="tooltip"]');
        if (tooltips.length > 0) {
            [].slice.call(tooltips).map(el => new bootstrap.Tooltip(el));
        }
    }
    // Lite YouTube Embeds
    document.addEventListener('click', function (e) {
        const target = e.target.closest('.lite-youtube');
        if (target && !target.querySelector('iframe')) {
            const videoId = target.getAttribute('data-video-id');
            target.innerHTML = `
                <iframe 
                    src="https://www.youtube.com/embed/${videoId}?rel=0" 
                    frameborder="0" 
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
                    allowfullscreen 
                    referrerpolicy="no-referrer-when-downgrade"
                    title="${target.getAttribute('aria-label') || 'YouTube Video'}">
                </iframe>`;
        }
    });
});
