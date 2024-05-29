# Connect LED to pin 8 + GND. Press the boot button to toggle the LED on and off.
from machine import Pin

led_on = True

led = Pin(8, Pin.OUT)


def write_led():
    if led_on:
        led.on()
    else:
        led.off()


def handle_button_interrupt(_):
    global led_on
    led_on = not led_on
    write_led()


write_led()
button = Pin(9, Pin.IN)
button.irq(trigger=Pin.IRQ_RISING, handler=handle_button_interrupt)
