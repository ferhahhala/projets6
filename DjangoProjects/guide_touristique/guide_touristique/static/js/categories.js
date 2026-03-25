function goHotels(){
    const wilaya = "{{ wilaya_name }}";
    window.location.href = `/hotels/?wilaya=${wilaya}`;
}

function goRestaurants(){
    const wilaya = "{{ wilaya_name }}";
    window.location.href = `/restaurants/?type=restaurant&wilaya=${wilaya}`;
}

function goFastFood(){
    const wilaya = "{{ wilaya_name }}";
    window.location.href = `/restaurants/?type=fastfood&wilaya=${wilaya}`;
}

function goPlaces(){
    const wilaya = "{{ wilaya_name }}";
    window.location.href = `/places/?wilaya=${wilaya}`;
}