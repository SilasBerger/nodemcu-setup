# Connect LED Pin 8 + GND. Press the boot button to toggle the LED on and off.
from machine import Pin

led_on = True
button_press_registered = False

led = Pin(8, Pin.OUT)
button = Pin(9, Pin.IN)

def write_led():
    if led_on:
        led.on()
    else:
        led.off()

write_led()

while(True):
    if button.value() == 0:
        if not button_press_registered:
            button_press_registered = True
            led_on = not led_on
            write_led()
    elif button_press_registered:
        button_press_registered = False
