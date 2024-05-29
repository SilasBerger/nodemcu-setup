# Connect LED to pin 8 + GND.
from machine import Pin
led = Pin(8, Pin.OUT)
led.on()

# You can also enter the REPL now and turn the LED off:
# picocom -b 115200 /dev/tty.usbmodem1101 (or appropriate USB port)
# >>> led.off()
