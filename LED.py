from machine import Pin
from time import sleep

led = Pin(2,Pin.OUT)
led1 = Pin(5,Pin.OUT)

led_state = True
led1_state = True

while True:
    led_state = not led_state
    led.value(led_state)
    led1_state = not led_state
    led1.value(led1_state)
    print("LED turned on" if led_state else "LED turned off")
    print("LED1 turned on" if led_state else "LED turned off")
    sleep(0.1)
    sleep(0.1)