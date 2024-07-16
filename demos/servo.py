# Connect servo to SERVO_PIN (orange PWM lead), 5V and GND and enter angles in REPL. Feel free to try angles < 1° or
# > 180°, since most 9g servos tend to respond to pulse widths between 500ms and 2500ms.

from machine import Pin, PWM


SERVO_PIN = 22
PWM_FREQ = 50  # Typically, 40-4000 Hz; higher frequencies lead to faster but less precise movements
PULSE_RANGE_MIN_US = 500
PULSE_RANGE_MAX_US = 2500
ANGLE_MAX = 180


def angle_to_duty_cycle(angle):
    pulse_width_us = PULSE_RANGE_MIN_US + (angle * (PULSE_RANGE_MAX_US - PULSE_RANGE_MIN_US) * (1/ANGLE_MAX))
    time_period_us = 1000000 / PWM_FREQ
    duty_cycle_decimal = pulse_width_us / time_period_us
    duty_cycle_u16 = int(duty_cycle_decimal * (2**16 - 1))
    print(f"angle={angle}°, pulse_width={pulse_width_us}, duty={duty_cycle_decimal * 100}%, duty_u16={duty_cycle_u16}")
    return duty_cycle_u16


servo = PWM(Pin(SERVO_PIN), freq=PWM_FREQ, duty_u16=angle_to_duty_cycle(0))


def servo_write(angle):
    servo.duty_u16(angle_to_duty_cycle(angle))


while True:
    angle = float(input(f"Angle (0-{ANGLE_MAX}): "))
    servo_write(angle)
