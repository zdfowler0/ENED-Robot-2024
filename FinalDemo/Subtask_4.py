#!/usr/bin/env python3

'''
This program will make the APR pick up the box,
then take it to the end of the row
'''

from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_D, MediumMotor, MoveDifferential, SpeedRPM
from ev3dev2.wheel import EV3EducationSetTire
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3
from ev3dev2.sensor.lego import GyroSensor, UltrasonicSensor
from ev3dev2.sound import Sound
from wheelbase import WHEEL_DISTANCE

# Size of a stud in MM
STUD_MM = 8
MM_IN = 25.4
# wheel distance
wheel_distance = WHEEL_DISTANCE

# Initilize robot system
mdiff = MoveDifferential(left_motor_port=OUTPUT_A, right_motor_port=OUTPUT_D, wheel_class=EV3EducationSetTire, wheel_distance_mm=wheel_distance)
mdiff.gyro = GyroSensor(INPUT_1)
motor = MediumMotor(OUTPUT_B)
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

mdiff.odometry_start()

# This function allows the robot to move a specified distance using the gyro for error correction
def go(distance_mm, angle, speed=40, accuracy=0.5):
    # turn to correct direction
    mdiff.turn_to_angle(SpeedRPM(speed/2), angle, brake=True, block=True, error_margin=accuracy, use_gyro=True)
    
    itterations = 5

    # move in that direction
    for i in range(itterations):
        mdiff.on_for_distance(SpeedRPM(speed), distance_mm / itterations)
        mdiff.turn_to_angle(SpeedRPM(speed/2), angle, brake=True, block=True, error_margin=accuracy, use_gyro=True)

'''
This is the code that runs the subtask
'''
# move to the box
while(ultrasonic.distance_centimeters > 5 and ultrasonic.distance_centimeters != 255):
    print(ultrasonic.distance_centimeters)
    mdiff.on_for_distance(SpeedRPM(15), 30)

while(ultrasonic.distance_centimeters > 3 and ultrasonic.distance_centimeters != 255):
    print(ultrasonic.distance_centimeters)
    mdiff.on_for_distance(SpeedRPM(15), 5)

print(ultrasonic.distance_centimeters)
mdiff.on_for_distance(SpeedRPM(10), 20)

spkr.play_song((
    ('E4', 'e'),
    ('E4', 'e')
))
# pick up the box
motor.on_for_rotations(SpeedRPM(-15), 1.25)
# back up
go(4*MM_IN, 90, speed=-20)
# go to end of aisle
mdiff.turn_left(SpeedRPM(10), 87, use_gyro=False)
mdiff.on_for_distance(SpeedRPM(20), 20 * MM_IN)
# place down
motor.on_for_rotations(SpeedRPM(20), 1.25)

# end odometry thread
mdiff.odometry_stop()