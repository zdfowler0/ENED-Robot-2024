#!/usr/bin/env python3

from ev3dev2.motor import OUTPUT_B, SpeedPercent, MediumMotor

motor = MediumMotor(OUTPUT_B)

# (-) is down
for i in range(2):
    motor.on_for_rotations(SpeedPercent(15), 1.25)
    motor.on_for_rotations(SpeedPercent(-15), 1.25)