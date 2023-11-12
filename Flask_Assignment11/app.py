from flask import Flask, render_template
from flask_socketio import SocketIO, emit, join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    """
    - Chat interface is implemented using SocketIO to render different sessions of chat into a single template
    - How to test?
        - Open different tabs in same browser/different browser, with same link "/"
        - Enter a username and chat room name
        - Say, Chat room name is "Chat_Room1"
        - For different users, try sending messages from different tabs, provided room name is same
        - Different messages will appear in the same window
        - Script handling is currently being done using JavaScript in the index.html itself
    """
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('join')
def handle_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    emit('message', {'username': 'System', 'message': f'{username} has joined the room.'}, room=room)
    emit('join_response', {'success': True}, callback=log_response)

@socketio.on('leave')
def handle_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    emit('message', {'username': 'System', 'message': f'{username} has left the room.'}, room=room)
    emit('leave_response', {'success': True}, callback=log_response)

def log_response(data):
    print(f"Response from client: {data}")

@socketio.on('message')
def handle_message(data):
    username = data['username']
    message = data['message']
    room = data['room']
    emit('message', {'username': username, 'message': message}, room=room)

if __name__ == '__main__':
    socketio.run(app, debug=True)
