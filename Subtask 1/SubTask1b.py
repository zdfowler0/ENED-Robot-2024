#!/usr/bin/env python3

from ev3dev2.motor import OUTPUT_A, OUTPUT_D, MoveTank, SpeedPercent, follow_for_ms
import math

# Make controls
moveDA = MoveTank(OUTPUT_D, OUTPUT_A)

# variables determined by subtask
num_laps = 5
distance_cm = 150

# variables we want to use
speed_percent = 30
distance_mm = distance_cm * 10

# wheel specifications (68.8mm is big, 56mm is med)
wheel_diameter = 56
wheel_circumference = 2*math.pi()*(wheel_diameter / 2)
rotations = distance_mm / wheel_circumference

# move a set number of rotations
def move(self, speed, rotations):
    self.on_for_rotations(speed,speed,rotations=rotations,brake=True)

# run the specified number of laps while turning at each end
for i in range(num_laps):
    move(moveDA, speed_percent, rotations)

    # turn
    moveDA.on_for_rotations(speed_percent,-speed_percent,rotations=1.5,brake=True)
