from machine import Pin
from time import sleep

input_test = Pin(15, Pin.IN, Pin.PULL_DOWN)

while True:
    print(input_test.value())
    sleep(0.5)
    