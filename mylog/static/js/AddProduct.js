document.addEventListener('DOMContentLoaded', function () {
    // Obtener elementos necesarios
    const continueBtn = document.getElementById('continueBtn');
    const section1 = document.getElementById('section1');
    const section2 = document.getElementById('section2');

    // Asegurarse de que los elementos existan antes de usarlos
    if (continueBtn && section1 && section2) {
        continueBtn.addEventListener('click', function() {
            // Obtener los valores de los campos de la primera sección
            const name = document.getElementById('name').value.trim();
            const description = document.getElementById('description').value.trim();
            const price = document.getElementById('price').value.trim();

            // Validación simple
            if (!name || !description || !price) {
                if (!name) document.getElementById('name').classList.add('input-error');
                if (!description) document.getElementById('description').classList.add('input-error');
                if (!price) document.getElementById('price').classList.add('input-error');
                alert('Por favor, complete todos los campos.');
                return; 
            }
            section1.style.display = 'none';
            section2.style.display = 'block';
        });
    }
});