from time import sleep
import socketio
import serial
import json
import sys

ser = serial.Serial()
ser.baudrate = 2400
ser.port = 'COM5'
ser.timeout = 10
ser.open()

def printStream():
	global stream
	stream = ser.readline()


sio = socketio.Client()

@sio.event
def connect():
	global connected
	connected = True
	print('connection establish')


@sio.event
def disconnect():
	print('disconecet from server')
	ser.close()

sio.connect('ws://server.c.gtco.team')
while connected:	
	printStream()
	my_json_obj = json.loads(ser.readline().decode('ascii').replace('\n',''))
	my_json_obj["ID"] = int(sys.argv[1])
	my_json = json.dumps(my_json_obj)
	sio.emit('recivePic', my_json)

