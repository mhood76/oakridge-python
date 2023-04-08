from machine import Pin
from time import sleep


led = Pin(25, Pin.OUT)
#led2 = Pin(16, Pin.OUT)
button = Pin(15, Pin.IN, Pin.PULL_DOWN)

while True:
    led.value(0)
    while button.value() == 1:
        led.toggle()
        #led2.toggle()
        sleep(0.1)
