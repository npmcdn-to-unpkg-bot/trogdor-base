from flask import Flask, render_template
from flask.ext.socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

@app.route('/')
def index():
    print("hi!")
    return render_template('index.html')

@socketio.on('my event')
def test(message):
    emit('my response', {"data" : "have some!"})

def sendUpdates():
    socketio.emit('status', {'data': 'here ya go'})

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0")