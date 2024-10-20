import machine
import time

led = machine.Pin(2, machine.Pin.OUT)  

def blink_led():
    while True:
        led.value(1)  
        time.sleep(0.1)
        led.value(0) 
        time.sleep(0.1)

blink_led()
