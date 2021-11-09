#!/usr/bin/python
import serial
from time import sleep

port = '/dev/ttyUSB0'
controller = serial.Serial(port,115200,timeout=5)

while True:
    msg = controller.readline().strip().decode('ascii')

    if msg != None and msg != "":
        msg = str(msg).split(',')
        if msg[2] == 0:
            msg[2] = False
        elif msg[2] == 1:
            msg[2] = True
        if msg[3] == 0:
            msg[3] = False
        elif msg[3] == 1:
            msg[3] = True
        print("x: {}, y: {}, Left: {}, Right: {}".format(msg[0], msg[1], msg[2], msg[3]))
    sleep(.1)
