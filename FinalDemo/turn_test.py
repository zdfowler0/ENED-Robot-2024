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
from math import atan, degrees
from time import sleep

# Size of a stud in MM
STUD_MM = 8
MM_IN = 25.4

# Initilize robot system
mdiff = MoveDifferential(left_motor_port=OUTPUT_A, right_motor_port=OUTPUT_D, wheel_class=EV3EducationSetTire, wheel_distance_mm=20.8 * STUD_MM)
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



# let user know they may take readings
display.text_pixels("Ready!",font=my_font)
display.update()

# initial
mdiff.turn_right(SpeedRPM(5), 17)
octave = color.color
if(octave == 1):
    octave == 3
elif(octave == 6):
    octave == 4
note_str = 'C' + str(octave)
spkr.play_song((
    (note_str, 'e'),
))

# step
mdiff.turn_left(SpeedRPM(5), 10)
octave = color.color
if(octave == 1):
    octave == 3
elif(octave == 6):
    octave == 4
note_str = 'C' + str(octave)
spkr.play_song((
    (note_str, 'e'),
))

mdiff.turn_left(SpeedRPM(5), 10)
octave = color.color
if(octave == 1):
    octave == 3
elif(octave == 6):
    octave == 4
note_str = 'C' + str(octave)
spkr.play_song((
    (note_str, 'e'),
))

mdiff.turn_left(SpeedRPM(5), 10)
octave = color.color
if(octave == 1):
    octave == 3
elif(octave == 6):
    octave == 4
note_str = 'C' + str(octave)
spkr.play_song((
    (note_str, 'e'),
))