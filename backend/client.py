import socketio


connected = False;

sio = socketio.Client()

@sio.event
def connect():
	connected = True;
	print('connection establish')



@sio.event
def my_messsage(data):
	print ('message recieved with',data)
	sio.emit('recivePic', {'response':'my response'})

@sio.event
def disconnect():
	print('disconecet from server')

sio.connect('ws://localhost:5000')
while (connected){

	sio.emit('recivePic', {'my response':'my response'})

}

	