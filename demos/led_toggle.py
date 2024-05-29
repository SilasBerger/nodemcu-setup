# Connect LED Pin 8 + GND. Press the boot button to toggle the LED on and off.
from machine import Pin

led_on = False
button_pressed = False

led = Pin(8, Pin.OUT)
button = Pin(9, Pin.IN)

while(True):
    if button.value() == 0:
        if not button_pressed:
            button_pressed = True
            led_on = not led_on
            if led_on:
                led.on()
            else:
                led.off()
    elif button_pressed:
        button_pressed = False
