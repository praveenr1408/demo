import machine
import time

led = machine.Pin(2, machine.Pin.OUT)  # Assuming GPIO2 is the LED pin

def blink_led():
    while True:
        led.value(1)  # Turn on LED
        time.sleep(3)
        led.value(0)  # Turn off LED
        time.sleep(3)

blink_led()
