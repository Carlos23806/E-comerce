function toggleEdit() {
    const form = document.getElementById('user-info-form');
    const editBtn = document.getElementById('edit-btn');
    const inputs = form.querySelectorAll('.info-edit');
    const displays = form.querySelectorAll('.info-display');

    if (editBtn.textContent === 'Editar') {
        editBtn.textContent = 'Cancelar';
        inputs.forEach(input => input.style.display = 'block');
        displays.forEach(display => display.style.display = 'none');
    } else {
        editBtn.textContent = 'Editar';
        inputs.forEach(input => input.style.display = 'none');
        displays.forEach(display => display.style.display = 'block');
    }
}