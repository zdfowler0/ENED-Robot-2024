#!/usr/bin/env python3

'''
This program will move the APR from the end of a row to box location 9,
scan the barcode,
deterine if the barcode is correct,
display the barcode that was read and if it is correct
'''

from ev3dev2.motor import OUTPUT_A, OUTPUT_D, MoveDifferential, SpeedRPM
from ev3dev2.wheel import EV3EducationSetTire
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3
from ev3dev2.sensor.lego import GyroSensor, UltrasonicSensor, ColorSensor
from ev3dev2.display import Display
from ev3dev2.sound import Sound
from ev3dev2.fonts import load
from wheelbase import WHEEL_DISTANCE
from math import atan, degrees
from time import sleep

# Size of a stud in MM
STUD_MM = 8
MM_IN = 25.4
# wheel distance
wheel_distance = WHEEL_DISTANCE

# Initilize robot system
mdiff = MoveDifferential(left_motor_port=OUTPUT_A, right_motor_port=OUTPUT_D, wheel_class=EV3EducationSetTire, wheel_distance_mm=wheel_distance)
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

# sensors
ultrasonic = UltrasonicSensor(INPUT_2)
color = ColorSensor(INPUT_3)

# Display screen for text
display = Display()
# load font for better readability
my_font = load("helvBO24")


mdiff.odometry_start()

# This function allows the robot to move a specified distance using the gyro for error correction
def go(distance_mm, angle, speed=40, accuracy=2):
    # turn to correct direction
    mdiff.turn_to_angle(SpeedRPM(speed/2), angle, brake=True, block=True, error_margin=0.5, use_gyro=True)
    
    itterations = 5

    # move in that direction
    for i in range(itterations):
        mdiff.on_for_distance(SpeedRPM(speed), distance_mm / itterations)
        mdiff.turn_to_angle(SpeedRPM(speed/2), angle, brake=True, block=True, error_margin=accuracy, use_gyro=True)


given_barcode = [1, 0, 1, 0]

'''
Barcode reading
'''
curr_barcode = []



# 1.5 in from right side



curr_barcode = []

# let user know they may take readings
display.text_pixels("Ready!",font=my_font)
display.update()

initial_angle = 20
sub_angle = initial_angle * 0.5

# initial
if(color.color == 1):
    curr_barcode.append(1)
    octave = 3
else:
    curr_barcode.append(0)
    octave = 4
note_str = 'C' + str(octave)
spkr.play_song((
    (note_str, 'e'),
))

# step
mdiff.turn_left(SpeedRPM(5), sub_angle)
if(color.color == 1):
    curr_barcode.append(1)
    octave = 3
else:
    curr_barcode.append(0)
    octave = 4
note_str = 'C' + str(octave)
spkr.play_song((
    (note_str, 'e'),
))

mdiff.turn_left(SpeedRPM(5), sub_angle)
if(color.color == 1):
    curr_barcode.append(1)
    octave = 3
else:
    curr_barcode.append(0)
    octave = 4
note_str = 'C' + str(octave)
spkr.play_song((
    (note_str, 'e'),
))

mdiff.turn_left(SpeedRPM(5), sub_angle)
if(color.color == 1):
    curr_barcode.append(1)
    octave = 3
else:
    curr_barcode.append(0)
    octave = 4
note_str = 'C' + str(octave)
spkr.play_song((
    (note_str, 'e'),
))

# turn to back out
mdiff.turn_to_angle(SpeedRPM(10), 90, error_margin=1, use_gyro=True)

new_barcode = [0, 0, 0, 0]
for i in range(3, 0, -1):
    new_barcode[3-i] = curr_barcode[i]


print(new_barcode)