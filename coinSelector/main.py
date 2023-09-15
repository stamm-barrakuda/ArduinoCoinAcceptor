import machine
import time

coinInput = machine.Pin(25, machine.Pin.IN,machine.Pin.PULL_UP)
while True:
    val = coinInput.value()
    if not val:
        print(1)
        time.sleep(0.05)