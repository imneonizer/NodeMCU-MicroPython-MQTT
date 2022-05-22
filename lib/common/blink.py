from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT); led.on()

def blink(n=1, s=0.1, start_off=True, stop_off=True):
    # blink onboard led based on given paremeters
    led.on() if stop_off else led.off()
    for i in range(n):
        if start_off:
            led.off(); sleep(s); led.on()
        else:
            led.on(); sleep(s); led.off()
        if i <= n: sleep(s)
    led.on() if stop_off else led.off()