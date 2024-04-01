#!/usr/bin/env python3

from ev3dev2.motor import OUTPUT_A, OUTPUT_D, MoveTank, SpeedPercent
from ev3dev2.sensor import INPUT_2
from ev3dev2.sensor.lego import UltrasonicSensor

# Make controls
moveDA = MoveTank(OUTPUT_D, OUTPUT_A)

# Speaker
sensor = UltrasonicSensor(INPUT_2)

# variables determined by subtask
step_distance_in = 1
#distance_cm = distance_in * 2.54
step_distance_cm = 2

# distance the robot should stop away from the object (cm)
stop_distance = 10

# variables we want to use
speed_percent = 30
step_distance_mm = step_distance_cm * 10

# wheel specifications (68.8mm is big, 56mm is medium)
wheel_diameter = 56
wheel_circumference = 2*3.1415926*(wheel_diameter / 2)
rotations = step_distance_mm / wheel_circumference

while(sensor.distance_centimeters_continuous > stop_distance):
        moveDA.on_for_rotations(speed_percent,speed_percent,rotations=rotations,brake=False)