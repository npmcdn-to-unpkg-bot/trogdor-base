var map;

$(document).ready(function(){
    var socket = io.connect();
    
    var map = L.map('map', {
        zoomControl: false,
        dragging: false,
        touchZoom: false,
        scrollWheelZoom: false,
        doubleClickZoom: false,
        boxZoom: false,
        keyboard: false
    });

    map.setZoom(18);

    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png').addTo(map);

    var centerMarker = L.marker([0,0]);
    centerMarker.addTo(map);

    socket.on('gps', function(message) {
        console.log(message);
        $('#time').html("Time (UTC): " + message.rmc.time);
        $('#coords').html(message.rmc.latitude.toFixed(6) + ', ' + message.rmc.longitude.toFixed(6));
        $('#speed').html("Speed (Knots): " + message.rmc.speed);
        $('#altitude').html("Altitude (M): " + message.gga.altitude);
        $('#satellites').html("Satellites: " + message.gga.satellites);
        $('#fix').html("Fix Quality: " + message.gga.fix_quality);
        map.setView([message.rmc.latitude, message.rmc.longitude]);
        centerMarker.setLatLng([message.rmc.latitude, message.rmc.longitude]);
    });

});
