#!/usr/bin/env python3

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1

'''
- The robot is front-wheel drive
- Motor A is on the right
- Motor D is on the left
'''

# Define large motors
motorA = LargeMotor(OUTPUT_A)
motorD = LargeMotor(OUTPUT_D)
motorDA = MoveTank(OUTPUT_D, OUTPUT_A)

'''
# Runs the motor on output A at 75% max speed for 5 rotations,
# then runs the motor on output D at 75% max speed for 5 rotations
motorA.on_for_rotations(SpeedPercent(75), 5)
motorD.on_for_rotations(SpeedPercent(75), 5)
'''

# Run both motors ay 75% max speed for 5 rotations
motorDA.on_for_rotations(75, 75, 5)

# Turn right
motorDA.on_for_rotations(75, -75, 5)

# Turn Left
motorDA.on_for_rotations(-75, 75, 5)
