from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index_notifications.html')

def send_notification(message):
    time.sleep(5)  # Simulate some processing time before sending the notification
    socketio.emit('notification', {'message': message}, namespace='/notifications')

@socketio.on('connect', namespace='/notifications')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect', namespace='/notifications')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('post_message')
def handle_post_message(data):
    message = data['message']
    print(f"Received message: {message}")
    send_notification(f'New message: {message}')

if __name__ == '__main__':
    socketio.run(app, debug=True)
