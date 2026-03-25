function renderEtablissements(data) {
    const container = document.getElementById('etablissements');
    container.innerHTML = '';
    data.forEach(e => {
        const card = document.createElement('div');
        card.classList.add('card');
        card.innerHTML = `
            <img src="${e.image}" alt="${e.nom}">
            <h3>${e.nom}</h3>
            <p>Prix: ${e.prix} DZD</p>
            <p>${e.localisation}</p>
            <a href="${e.lienMap}" target="_blank">Voir sur Google Maps</a>
        `;
        container.appendChild(card);
    });
}