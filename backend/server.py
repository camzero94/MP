import json
import os
from time import time
import datetime
from flask import Flask 
from flask_socketio import SocketIO, emit,send
from engineio.payload import Payload
Payload.max_decode_packets = 50

global_arr = []
curr_obj = {}

_aux = 0
app = Flask(__name__, static_url_path="")
app.config['SECRET KEY'] = 'secret!'
socketio = SocketIO(app,cors_allowed_origins = "*")
app.debug = True

db = {}

mess = "Message sended from server to client"
@socketio.on('connect')
def test_connect():
	print('Client Connected')


@socketio.on('disconnect')
def test_disconnecte():
	print('Client Disconnected')

@socketio.on('recivePic')
def test_connect(data):
	global curr_obj
	curr_obj = json.loads(data)
	print('Message is : ' + str(data))
	db[curr_obj["ID"]] = {key:value for key, value in curr_obj.items() if key != "ID"}
	db[curr_obj["ID"]]["last_update"] = str(datetime.datetime.utcnow())
	socketio.emit('sendPic_message', json.dumps(db))


@socketio.on('sendPic_message')
def handle_message(message):
	send(message)



if __name__ == "__main__":
    port = os.environ.get("PORT", 5000)
    socketio.run(app,host="0.0.0.0",port=port)
#     app.run(host="0.0.0.0", port=port, debug=True)
