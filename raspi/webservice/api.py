import gps
import serial
from threading import Thread
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app, async_mode='threading')
thread = None

def background_loop():
    port = "/dev/ttyUSB0"
    baud = 9600
    timeout = 10
    ser = serial.Serial(port, baud, timeout=timeout)

    while True:
        reading = ser.readline().decode("utf-8").split(',')
        if (reading[0] == "$GPRMC"):
            lat = gps.latitude(reading)
            lon = gps.longitude(reading)
            socketio.emit('gps', {'latitude' : lat, 'longitude' : lon})
        elif (reading[0] == "$GPGSV"):
            if (int(reading[2]) == 1):
                sats = gps.satellites(reading)
                socketio.emit('satellites', {'satellites' : sats})

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def connected():
    print("connected")
    global thread
    if thread is None:
        thread = socketio.start_background_task(target=background_loop)

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", debug=True)