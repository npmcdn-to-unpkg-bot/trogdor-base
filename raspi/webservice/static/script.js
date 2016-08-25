var map;

$(document).ready(function(){
    var socket = io.connect();
    
    var map = L.map('map');

    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png').addTo(map);

    var centerMarker = L.marker([0,0]);
    centerMarker.addTo(map);

    socket.on('gps', function(message) {
        console.log(message);
        $('#time').html("Time (UTC): " + message.time);
        $('#coords').html(message.latitude + ', ' + message.longitude);
        map.setView([message.latitude, message.longitude], 18);
        centerMarker.setLatLng([message.latitude, message.longitude]);
    });

    socket.on('satellites', function(message) {
        console.log(message);
        $('#satellites').html("Satellites: " + message.satellites);
    });

});
