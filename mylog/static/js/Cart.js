function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function updateCartItem(input) {
    const itemId = input.name.split('-')[1];
    const quantity = input.value;
    const csrfToken = getCookie('csrftoken');
    
    input.parentElement.classList.add('updating');
    
    fetch('/cart/update/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify({
            item_id: itemId,
            quantity: quantity
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            const itemTotal = input.closest('.item-details').querySelector('.total');
            const cartTotal = document.querySelector('.cart-total h3');
            itemTotal.textContent = `Total: $${data.item_total}`;
            cartTotal.textContent = `Total: $${data.cart_total}`;
        }
    })
    .finally(() => {
        input.parentElement.classList.remove('updating');
    });
}

document.addEventListener('DOMContentLoaded', function() {
    const quantityInputs = document.querySelectorAll('.quantity-control input');
    quantityInputs.forEach(input => {
        input.addEventListener('change', () => updateCartItem(input));
    });
});