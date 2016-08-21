$(document).ready(function(){
    var socket = io.connect();

    socket.on('gps', function(message) {
        console.log(message);
        $('#log').append(message.latitude + ', ' + message.longitude + '<br/>');
    });

});
