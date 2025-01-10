document.addEventListener('DOMContentLoaded', function() {
    const loginContainer = document.getElementById('loginContainer');
    const registerContainer = document.getElementById('registerContainer');
    const showRegisterBtn = document.getElementById('showRegister');
    const showLoginBtn = document.getElementById('showLogin');

    // Función para cambiar entre formularios
    function switchForm(showRegister) {
        if (showRegister) {
            loginContainer.style.transform = 'translateX(-100%)';
            registerContainer.style.transform = 'translateX(-100%)';
        } else {
            loginContainer.style.transform = 'translateX(0)';
            registerContainer.style.transform = 'translateX(0)';
        }
    }

    // Event listeners para los botones de cambio
    showRegisterBtn.addEventListener('click', () => switchForm(true));
    showLoginBtn.addEventListener('click', () => switchForm(false));

    // Lógica de validación para la primera sección
    const continueBtn = document.getElementById('continueBtn');
    const section1 = document.getElementById('section1');
    const section2 = document.getElementById('section2');
    
    continueBtn.addEventListener('click', function() {
        const username = document.getElementById('username').value.trim();
        const name = document.getElementById('name').value.trim();
        const lastName = document.getElementById('last_name').value.trim();
        
        if (!username || !name || !lastName) {
            alert('Por favor, complete todos los campos.');
            return;
        }

        // Ocultar la sección 1 y mostrar la sección 2
        section1.style.display = 'none';
        section2.style.display = 'block';
    });

    // Manejar mensajes de alerta
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.opacity = '0';
            setTimeout(() => alert.remove(), 300);
        }, 5000);
    });
});
