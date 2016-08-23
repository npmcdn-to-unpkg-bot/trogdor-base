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
    g = gps.GPS('/dev/ttyUSB0', 9600, 10);
    while True:
        g.parse()
        socketio.emit('gps', g.get_json())

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