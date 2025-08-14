// Index Page JavaScript

document.addEventListener('DOMContentLoaded', function() {
    initializeIndexPage();
});

function initializeIndexPage() {
    // Initialize animations
    initializeAnimations();
    
    // Initialize counter animations
    initializeCounterAnimations();
    
    // Initialize parallax effects
    initializeParallaxEffects();
    
    // Initialize enhanced hover effects
    initializeHoverEffects();
    
    // Initialize smooth scrolling
    initializeSmoothScrolling();
}

function initializeCounterAnimations() {
    // Initialize counter animations for stats
    const statCards = document.querySelectorAll('.stat-card');
    
    statCards.forEach(card => {
        const numberElement = card.querySelector('.stat-number');
        if (numberElement) {
            const target = parseInt(numberElement.getAttribute('data-target')) || 0;
            numberElement.textContent = '0'; // Start at 0
        }
    });
}

function initializeAnimations() {
    // Intersection Observer for animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                
                // Trigger counter animation for stats
                if (entry.target.classList.contains('stat-card')) {
                    animateCounter(entry.target);
                }
            }
        });
    }, observerOptions);
    
    // Observe all fade-in elements
    document.querySelectorAll('.fade-in').forEach(el => {
        observer.observe(el);
    });
    
    // Trigger hero animations immediately
    setTimeout(() => {
        document.querySelectorAll('.hero-content .fade-in').forEach((el, index) => {
            setTimeout(() => {
                el.classList.add('visible');
            }, index * 200); // Stagger the animations
        });
    }, 100);
}

function animateCounter(statCard) {
    const numberElement = statCard.querySelector('.stat-number');
    const target = parseInt(numberElement.getAttribute('data-target'));
    const duration = 1500; // 1.5 seconds (reduced from 2s)
    const step = target / (duration / 16); // 60fps
    let current = 0;
    
    const timer = setInterval(() => {
        current += step;
        if (current >= target) {
            current = target;
            clearInterval(timer);
        }
        numberElement.textContent = Math.floor(current);
    }, 16);
}

function initializeParallaxEffects() {
    // Parallax effect for floating shapes
    let ticking = false;
    
    function updateParallax() {
        const scrolled = window.pageYOffset;
        const shapes = document.querySelectorAll('.shape');
        
        shapes.forEach((shape, index) => {
            const speed = 0.3 + (index * 0.1); // Reduced speed for better performance
            shape.style.transform = `translateY(${scrolled * speed}px)`;
        });
        
        ticking = false;
    }
    
    window.addEventListener('scroll', () => {
        if (!ticking) {
            requestAnimationFrame(updateParallax);
            ticking = true;
        }
    });
}

function initializeHoverEffects() {
    // Enhanced hover effects for feature cards
    document.querySelectorAll('.feature-card').forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-4px) scale(1.02)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });
}

function initializeSmoothScrolling() {
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// Performance optimizations
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Optimized scroll handler
const optimizedScrollHandler = debounce(() => {
    // Any scroll-based functionality can be added here
}, 16); // ~60fps

window.addEventListener('scroll', optimizedScrollHandler);
