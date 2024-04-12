#!/usr/bin/env python3

'''
This program should be run at the begining of
the tests to calibrate the gyro sensor
'''

from ev3dev2.motor import OUTPUT_A, OUTPUT_D, MoveDifferential, SpeedRPM
from ev3dev2.wheel import EV3EducationSetTire
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.sound import Sound
from wheelbase import WHEEL_DISTANCE
from math import pi

# Size of a stud in MM
STUD_MM = 8
# MM to IN conversion
MM_IN = 25.4
# wheel distance
wheel_distance = WHEEL_DISTANCE

mdiff = MoveDifferential(left_motor_port=OUTPUT_A, right_motor_port=OUTPUT_D, wheel_class=EV3EducationSetTire, wheel_distance_mm= wheel_distance)
mdiff.gyro = GyroSensor(INPUT_1)
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

# Go in a 200 mm circle
mdiff.on_arc_right(speed=SpeedRPM(40), radius_mm=200, distance_mm=2*pi*200, brake=True, block=True)