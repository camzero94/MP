import os 
from flask import Flask 

from flask_socketio import SocketIO, emit,send,join_room,leave_room

_aux = 0
app = Flask(__name__, static_url_path="")
app.config['SECRET KEY'] = 'secret!'
socketio = SocketIO(app,cors_allowed_origins = "*")
app.debug = True

mess = "Message sended from server to client"
@socketio.on('connect')
def test_connect():
	print('Client Connected')


@socketio.on('disconnect')
def test_disconnecte():
	print('Client Disconnected')

@socketio.on('recivePic')
def test_connect(data):
	print('Message is : ' + str(data))

@socketio.on('sendPic_message')
def handle_message(message):
	send(message)

def send_basic_message():
	global _aux 
	_aux = _aux + 1
	socketio.emit('sendPic_message', f"hello world {_aux}")

@socketio.on('client_message')
def handle_messge(message):
	send_basic_message()
# @socketio.on('join')
# def on_join(data):
#     username = data['username']
#     room = data['room']
#     join_room(room)
#     send(username + ' has entered the room.', to=room)

# @socketio.on('leave')
# def on_leave(data):
#     username = data['username']
#     room = data['room']
#     leave_room(room)
#     send(username + ' has left the room.', to=room)


if __name__ == "__main__":
    port = os.environ.get("PORT", 5000)
    socketio.run(app,host="0.0.0.0",port=port)
#     app.run(host="0.0.0.0", port=port, debug=True)
