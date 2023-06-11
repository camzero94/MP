
<p align="center"><img width=70% src="https://github.com/camzero94/MP/blob/main/media/Pic_Title.png"></p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![React](https://img.shields.io/badge/react-v18+-blue.svg)
![Flask-SocketIO](https://img.shields.io/badge/flaskSocketIO-v5.1.1+-blue.svg)
![Assemble](https://img.shields.io/badge/Assembly-lenguage+-blue.svg)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)





# Basic Overview
An implementation for the 4.0 industry of the Pic-F18520 as a sensor of temperature and light that connects to a web server via Socket protocol.

## Features
- Innovative way of connect the the PIC-F18520 via socket protocol to "push" data to the forntend client via the socket protocol.
- It will help industries where enviroment is a key factor in the quality of the final product.
## Architecture
<p align="center"><img width=70% src="https://github.com/camzero94/MP/blob/main/media/PIC.drawio.svg"></p>

## Prerequisites
- Python 3.8 or later.
- Pyserial 3.5
- Flask-SocketIO
- Pipenv
- Python-engineio 4.3.1

## Installation and Usage
* Connect the PIC-F18520 to the your local machine to one of the USB ports, then search in the Device Manager for the COM port of where it is connected.
* Run pip install -r requirements.txt
* Run source backend/env_mp/bin/activate to start the enviroment. 
* Run python3 client.py to make the PIC-F18520 start collecting the information of the enviroment, then send it to the web server and finally being pushed to the web server.

# Author 
## Camilo Quiñones
