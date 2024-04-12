#!/usr/bin/env python3

'''
This program will move the AMR from Home B, (102 in, -6in)
then go to Home A (6 in, -6 in)
'''

from ev3dev2.motor import OUTPUT_A, OUTPUT_D, MoveDifferential, SpeedRPM
from ev3dev2.wheel import EV3EducationSetTire
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.sound import Sound
from wheelbase import WHEEL_DISTANCE
from time import sleep

# Size of a stud in MM
STUD_MM = 8
MM_IN = 25.4
# wheel distance
wheel_distance = WHEEL_DISTANCE

# Initilize robot system
mdiff = MoveDifferential(left_motor_port=OUTPUT_A, right_motor_port=OUTPUT_D, wheel_class=EV3EducationSetTire, wheel_distance_mm=wheel_distance)
mdiff.gyro = GyroSensor(INPUT_1)
mdiff.odometry_start()
spkr = Sound()
spkr.play_song((
    ('C3', 'e'),
    ('G3', 'e')
))
mdiff.gyro.calibrate()
mdiff.gyro.reset()
spkr.play_song((
    ('G3', 'e'),
    ('C4', 'e')
))

# This function allows the robot to move a specified distance using the gyro for error correction
def go(distance_mm, angle, speed=40, accuracy=2):
    # turn to correct direction
    mdiff.turn_to_angle(SpeedRPM(speed/2), angle, brake=True, block=True, error_margin=0.5, use_gyro=True)
    
    itterations = 5

    # move in that direction
    for i in range(itterations):
        mdiff.on_for_distance(SpeedRPM(speed), distance_mm / itterations)
        mdiff.turn_to_angle(SpeedRPM(speed/2), angle, brake=True, block=True, error_margin=accuracy, use_gyro=True)

'''
This is the code that runs the subtask
'''
# go to the row (12 in)
go(12*MM_IN, 270)

# go to the end of the facility (96 in)
go(96*MM_IN, 0)

# go down into Home A (12 in)
go(12*MM_IN, 90)

# end odometry thread
mdiff.odometry_stop()