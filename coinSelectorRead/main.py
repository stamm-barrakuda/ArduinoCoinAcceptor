import time

import serial
from pynput.keyboard import Controller

ser = serial.Serial('COM5', 9600)
# read the serial connection
keyboard = Controller()
c = 0
while True:
    byt = ser.readline()
    counter = int(byt.decode())
    for _ in range(counter):
        keyboard.press('a')
        time.sleep(0.01)
        keyboard.release('a')
