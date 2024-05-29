# Connect LED to pin 8 + GND. Press the boot button to toggle between the different dimming steps.

import time
from machine import Pin, PWM

STEPS = [0, 8, 15, 50, 100]
DEBOUNCE_DELAY_MS = 100

t_last_interrupt = 0


def duty_cycle(duty_percentage):
    return min(2**16 - 1, int(2**16 * duty_percentage / 100))


duty_cycle_index = 0
led = PWM(Pin(8), freq=5000, duty_u16=duty_cycle(STEPS[duty_cycle_index]))


def update_brightness():
    global duty_cycle_index
    duty_cycle_index = (duty_cycle_index + 1) % len(STEPS)
    new_cycle = duty_cycle(STEPS[duty_cycle_index])
    print("New cycle:", new_cycle)
    led.duty_u16(new_cycle)


def handle_button_interrupt(_):
    global t_last_interrupt
    now = time.time_ns() / 1000
    if now - t_last_interrupt < DEBOUNCE_DELAY_MS:
        return

    t_last_interrupt = now
    update_brightness()


button = Pin(9, Pin.IN)
button.irq(trigger=Pin.IRQ_RISING, handler=handle_button_interrupt)
