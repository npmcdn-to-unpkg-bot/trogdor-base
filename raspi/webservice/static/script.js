var map;

$(document).ready(function(){
    var socket = io.connect();
    
    var map = L.map('map');
    map.setView([51.505, -0.09], 18);

    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png').addTo(map);

    socket.on('gps', function(message) {
        console.log(message);
        $('#log').append(message.latitude + ', ' + message.longitude + '<br/>');
    });
    
});
