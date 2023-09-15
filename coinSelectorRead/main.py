import time

import serial
from pynput.keyboard import Controller

ser = serial.Serial('/dev/ttyACM0', 9600)
# read the serial connection
keyboard = Controller()
c = 0
while True:
    byt = ser.readline()
    counter = int(byt.decode())
    for _ in range(counter):
        c += 1
        if c < 5:
            continue
        c = 0
        keyboard.press('a')
        time.sleep(0.02)
        keyboard.release('a')
        time.sleep(0.02)