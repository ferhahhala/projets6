// ================= Search Filter =================
const searchInput = document.getElementById('searchInput');
if(searchInput) {
    searchInput.addEventListener('keyup', function() {
        const filter = searchInput.value.toLowerCase();
        const cards = document.querySelectorAll('.card');
        cards.forEach(card => {
            const text = card.querySelector('h3').innerText.toLowerCase();
            card.style.display = text.includes(filter) ? '' : 'none';
        });
        searchInput.addEventListener('keydown', function(e){

        if(e.key === "Enter"){

            e.preventDefault(); 

            const hotel = searchInput.value.trim();

            if(hotel !== ""){

                const wilaya = localStorage.getItem("wilaya") || "";

                const query = hotel + " " + wilaya;

                const url = "https://www.google.com/maps/search/" + encodeURIComponent(query);

                window.open(url, "_blank");
            }
        }


    });
});
}

// ================= Toggle Favorite Heart =================
function toggleFavorite(el) {
    el.classList.toggle('filled');
    el.innerText = el.classList.contains('filled') ? '♥' : '♡';
}