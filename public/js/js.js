
window.onload = function(){
    var options = {
        zoom: 13
        , center: new google.maps.LatLng(12.142488, -86.2503468)
        , mapTypeId: google.maps.MapTypeId.MAP
    };
    var map = new google.maps.Map(document.getElementById('map_canvas'), options);
};