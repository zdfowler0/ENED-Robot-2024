#!/usr/bin/env python3

'''
This program will move the AMR from Home A, (6 in, -6in)
to the desired box location,
stop for 5 seconds,
then go to Home B (102 in, -6 in)
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
### Box location given in Subtask (7 - 12) ###
box_location = 9

box_location -= 6

# go to the begining of the row (30 in)
go(34*MM_IN, 90)

# go down the row to the specified box (each box is 6 in)
go((3 + (box_location*6)) * MM_IN, 0)

### PAUSE FOR 5 SECONDS
spkr.play_song((
    ('G#4', 'e'),
    ('C4', 'e')
))
sleep(5)

# go to the end of the facility ()
go((96 - (3 + (box_location*6)) + 1)*MM_IN, 0)

# # go down into Home B
go(34*MM_IN, -90)
spkr.play_song((
    ('C4', 'e'),
    ('C4', 'e')
))

# end odometry thread
mdiff.odometry_stop()