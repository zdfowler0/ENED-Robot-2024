#!/usr/bin/env python3

from ev3dev2.motor import OUTPUT_A, OUTPUT_D, MoveTank, SpeedPercent, follow_for_ms
from ev3dev2.sensor.lego import GyroSensor
import math

# Make controls
moveDA = MoveTank(OUTPUT_D, OUTPUT_A)

# variables determined by subtask
num_laps = 0
distance_cm = 0

# variables we want to use
speed_percent = 30
distance_mm = distance_cm * 10

# wheel specifications (68.8mm is big, 56mm is medium)
wheel_diameter = 56
wheel_circumference = 2*math.pi()*(wheel_diameter / 2)
rotations = distance_mm / wheel_circumference

# move a set number of rotations
def move(self, speed, rotations):
    self.on_for_rotations(speed,speed,rotations=rotations,brake=True)

# run the specified number of laps
for i in range(num_laps):
    if(i % 2 == 0):
        move(moveDA, speed_percent, rotations)
    else:
        move(moveDA, -speed_percent, rotations)
