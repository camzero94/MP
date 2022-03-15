# PIC-F18520 as a sensor of temperature and light that connects via socket protocol to a web server in the cloud
An implementation for the 4.0 industry of the Pic-F18520 as a sensor of temperature and light that connects to a web server via Socket protocol.

## Features
- Innovative way of connect the the PIC-F18520 via socket protocol to "push" data to the forntend client via the socket protocol.
- It will help industries where enviroment is a key factor in the quality of the final product.

## Prerequisites
- Python 3.8 or later.
- Pyserial 3.5
- Flask-SocketIO
- Pipenv
- Python-engineio 4.3.1

## How to Start 
* Connect the PIC-F18520 to the your local machine to one of the USB ports, then search in the Device Manager for the COM port of where it is connected.
* Run pip install -r requirements.txt
* Run source backend/env_mp/bin/activate to start the enviroment. 
* Run python3 client.py to make the PIC-F18520 start collecting the information of the enviroment, then send it to the web server and finally being pushed to the web server.

## Run the server 
Both the server and the client are already deploy inhttp://iot.c.gtco.team/    

# Author 
## Camilo Quiñones
