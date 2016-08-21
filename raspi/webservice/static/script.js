var map;

$(document).ready(function(){
    var socket = io.connect();
    
    var map = L.map('map');
    // map.setView([51.505, -0.09], 18);

    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png').addTo(map);

    socket.on('gps', function(message) {
        console.log(message);
        $('#coords').html(message.latitude + ', ' + message.longitude);
        map.setView([message.latitude, message.longitude], 18);
    });
    
});
