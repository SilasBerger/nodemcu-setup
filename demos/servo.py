# Connect servo to SERVO_PIN (orange PWM lead), 5V and GND and enter angles in REPL. Feel free to try angles < 1° or
# > 180°, since most 9g servos tend to respond to pulse widths between 500ms and 2500ms.

from machine import Pin, PWM


SERVO_PIN = 8
PWM_FREQ = 50  # Typically, 40-4000 Hz; higher frequencies lead to faster but less precise movements


def angle_to_duty_cycle(angle):
    pulse_width_ms = angle * (1 / 180) + 1  # 0° angle <-> 1ms pulse / 180° angle <-> 2ms pulse
    time_period_ms = 1000 / PWM_FREQ
    duty_cycle_decimal = pulse_width_ms / time_period_ms
    duty_cycle_u16 = int(duty_cycle_decimal * (2**16 - 1))
    print(f"angle={angle}°, pulse_width={pulse_width_ms}, duty={duty_cycle_decimal * 100}%, duty_u16={duty_cycle_u16}")
    return duty_cycle_u16


servo = PWM(Pin(SERVO_PIN), freq=PWM_FREQ, duty_u16=angle_to_duty_cycle(0))


def servo_write(angle):
    servo.duty_u16(angle_to_duty_cycle(angle))


while True:
    angle = float(input("Angle (usually 0-180): "))
    servo_write(angle)
