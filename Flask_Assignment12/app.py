from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import random
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!' # Feel free to change it to any more strong secrets as per requirement
socketio = SocketIO(app)

@app.route('/')
def index():
    """
    - For explanation purposes, I have done random number generation
    - Generates the updated random number after every 3 seconds
    - Random number range will be between 1 to 100 at this time, can be changed accordingly
    - More real-time scenarios can be possible, but this was a basic example to get started
    - Socket connections are used to maintain the state of the APIs
    """
    return render_template('index.html')

def update_data():
    while True:
        time.sleep(3)  # Update data every 3 seconds
        data = {'value': random.randint(1, 100)}
        socketio.emit('update', data, namespace='/test')

@socketio.on('connect', namespace='/test')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect', namespace='/test')
def handle_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.start_background_task(target=update_data)
    socketio.run(app, debug=True)
