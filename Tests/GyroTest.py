#!/usr/bin/env python3

from ev3dev2.sensor import INPUT_4
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.led import Leds

gs = GyroSensor()
leds = Leds()

# Resets the gyro angle to 0
gs.reset()

while True:
    # Tests if the robot is facing the original direction
    if(gs.angle == 0 or gs.angle % 360 == 0):
        leds.set_color("LEFT", "GREEN")
        leds.set_color("RIGHT", "GREEN")
    # Tests if the robot is facing directly away from the original direction
    elif(gs.angle == 180 or gs.angle % 180 == 0):
        leds.set_color("LEFT", "RED")
        leds.set_color("RIGHT", "RED")
    elif(gs.angle > 0):
        leds.set_color("LEFT", "RED")
        leds.set_color("RIGHT", "GREEN")
    else:
        leds.set_color("LEFT", "GREEN")
        leds.set_color("RIGHT", "RED")
    
    '''
    # Flashes Amber is the robot is moving faster than 45 deg/sec
    if(abs(gs.rate) > 45):
        leds.set_color("LEFT", "AMBER")
        leds.set_color("RIGHT", "AMBER")
    '''
