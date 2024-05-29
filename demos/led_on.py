# Configure GPIO pin 8 as output and set to HIGH.
from machine import Pin
pin8 = Pin(8, Pin.OUT)
pin8.on()
