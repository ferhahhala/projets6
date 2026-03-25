const exploreBtn = document.getElementById("exploreBtn");
const select = document.getElementById("wilayaSelect");

// disabled
exploreBtn.classList.add("disabled");

// select wilaya
select.addEventListener("change", function(){
    if(select.value !== ""){
        exploreBtn.classList.remove("disabled");
    } else {
        exploreBtn.classList.add("disabled");
    }
});

// click
exploreBtn.addEventListener("click", function(e){

    const wilaya = select.value;

    if(wilaya === ""){
        e.preventDefault(); 
        alert("Choisissez une wilaya");
        return;
    }
    let historique = JSON.parse(localStorage.getItem("historique")) || [];

    if (!historique.includes(wilaya)) {
        historique.push(wilaya);
    }

    localStorage.setItem("historique", JSON.stringify(historique));

    localStorage.setItem("wilaya", wilaya);
    window.location.href = "categories.html";
});
    window.addEventListener("pageshow", function () {
    select.value = "";
    exploreBtn.classList.add("disabled");
});
