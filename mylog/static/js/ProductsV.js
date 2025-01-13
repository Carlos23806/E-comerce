document.addEventListener('DOMContentLoaded', function () {
    const cards = document.querySelectorAll('.card');
    const loadMoreBtn = document.getElementById('loadMoreBtn');
    const productsPerLoad = 30;
    let currentlyShown = 0;

    function loadMore() {
        const start = currentlyShown;
        const end = Math.min(start + productsPerLoad, cards.length);

        for (let i = start; i < end; i++) {
            cards[i].classList.add('visible');
            cards[i].style.display = 'flex';
        }

        currentlyShown = end;
        if (currentlyShown >= cards.length) {
            loadMoreBtn.classList.add('hidden');
        }
    }
    loadMore();

    loadMoreBtn.addEventListener('click', loadMore);
    if (cards.length <= productsPerLoad) {
        loadMoreBtn.classList.add('hidden');
    }
});