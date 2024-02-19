#!/usr/bin/env python3

from ev3dev2.motor import OUTPUT_A, OUTPUT_D, MoveTank, SpeedPercent
from ev3dev2.sound import Sound

# Make controls
moveDA = MoveTank(OUTPUT_D, OUTPUT_A)
# Speaker
spkr = Sound()

# variables determined by subtask
num_laps = 3
distance_cm = 120

# variables we want to use
speed_percent = 30
distance_mm = distance_cm * 10

# wheel specifications (68.8mm is big, 56mm is medium)
wheel_diameter = 68.8
wheel_circumference = 2*3.1415926*(wheel_diameter / 2)
rotations = distance_mm / wheel_circumference
'''
# move a set number of rotations
def move(self, speed, rotations):
    self.on_for_rotations(speed,speed,rotations=rotations,brake=True)
'''
# run the specified number of laps
for i in range(num_laps*2):
    if(i % 2 == 0):
        spkr.play_song((
            ('D4', 'e'),
            ('E4', 'e'),
            ('F#4', 'e'),
        ),tempo=240)        
        moveDA.on_for_rotations(speed_percent,speed_percent,rotations=rotations,brake=True)
    else:
        spkr.play_song((
            ('F#4', 'e'),
            ('E4', 'e'),
            ('D4', 'e'),
        ), tempo=240)
        moveDA.on_for_rotations(-speed_percent,-speed_percent,rotations=rotations*1,brake=True)
