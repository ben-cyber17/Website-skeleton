document.addEventListener('DOMContentLoaded', () => {
    
    // --- 1. VALIDAZIONE EMAIL IN TEMPO REALE ---
    const emailField = document.querySelector('input[type="email"]');
    if (emailField) {
        emailField.addEventListener('input', () => {
            const emailValue = emailField.value;
            const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            
            if (emailPattern.test(emailValue)) {
                emailField.style.borderColor = "#27ae60"; // Verde se valida
                emailField.style.backgroundColor = "#f1fdf6";
            } else {
                emailField.style.borderColor = "#e74c3c"; // Rosso se errata
                emailField.style.backgroundColor = "#fdf2f1";
            }
        });
    }

    // --- 2. ANIMAZIONI ON SCROLL (Apparizione fluida) ---
    const observerOptions = {
        threshold: 0.1 // L'animazione parte quando il 10% dell'elemento è visibile
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = "1";
                entry.target.style.transform = "translateY(0)";
            }
        });
    }, observerOptions);

    // Selezioniamo le card dei prodotti e delle tecnologie
    const cards = document.querySelectorAll('.prodotto-card, .tecnologia-item');
    cards.forEach(card => {
        // Stato iniziale "invisibile"
        card.style.opacity = "0";
        card.style.transform = "translateY(30px)";
        card.style.transition = "all 0.6s ease-out";
        observer.observe(card);
    });

    // --- 3. CAMBIO TITOLO SCHEDA (Tab Attention) ---
    // Quando l'utente cambia scheda del browser, il titolo cambia per attirare attenzione
    const originalTitle = document.title;
    window.addEventListener('blur', () => {
        if (window.location.pathname !== '/') {
            document.title = " Torna a trovarci! ";
        }
    });
    window.addEventListener('focus', () => {
        document.title = originalTitle;
    });

    console.log("JavaScript caricato correttamente! ");
});

// --- 4. GESTIONE CARICAMENTO FORM ---
const contactForm = document.querySelector('form');
const submitBtn = document.querySelector('.btn-invia');

if (contactForm && submitBtn) {
    // Creiamo l'elemento spinner dinamicamente
    const spinner = document.createElement('div');
    spinner.className = 'spinner';
    submitBtn.appendChild(spinner);

    contactForm.addEventListener('submit', () => {
        // Mostriamo lo spinner e disabilitiamo il tasto
        spinner.style.display = 'inline-block';
        submitBtn.classList.add('btn-loading');
        submitBtn.innerHTML = 'Invio in corso...';
        submitBtn.appendChild(spinner);
    });
}