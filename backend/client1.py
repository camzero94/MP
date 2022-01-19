import sys 
import json
from time import sleep
import socketio
import random

sio= socketio.Client()
my_json_obj = {}
def generateClient():

	global my_json_obj
	my_json_obj["light voltage"] = round(random.uniform(0.3,4.5),6)
	my_json_obj["temp"] = round(random.uniform(15.0,26.0),6)


@sio.event
def connect():
	global connected
	connected = True
	print('connection establish')

@sio.event
def disconnect():
	print('disconecet from server')

sio.connect('ws://10.7.209.158:5000')

while connected:
	generateClient()
	my_json_obj["ID"] = int(sys.argv[1])
	my_json = json.dumps(my_json_obj)
	sio.emit('recivePic', my_json)
	sleep(0.5)	

