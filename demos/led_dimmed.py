from machine import Pin, PWM

steps = [0, 1, 5, 10, 20, 60, 100]
button_press_registered = False

def duty_cycle(duty_percentage):
    return min(2**16 - 1, int(2**16 * duty_percentage / 100))

duty_cycle_index = 0
led = PWM(Pin(8), freq=5000, duty_u16=duty_cycle(steps[duty_cycle_index]))

def update_brightness(_):
    global duty_cycle_index
    duty_cycle_index = (duty_cycle_index + 1) % len(steps)
    new_cycle = duty_cycle(steps[duty_cycle_index])
    print("New cycle:", new_cycle)
    led.duty_u16(new_cycle)

button = Pin(9, Pin.IN)
button.irq(trigger=Pin.IRQ_RISING, handler=update_brightness)
