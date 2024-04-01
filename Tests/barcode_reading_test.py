#!/usr/bin/env python3

from ev3dev2.sensor import INPUT_3
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.button import Button
from ev3dev2.display import Display
from ev3dev2.fonts import load
import time

# load font for better readability
my_font = load("helvBO24")

# Sensor
sensor = ColorSensor(INPUT_3)
# Buttons to detect when to take an input
buttons = Button()
# Display screen for text
display = Display()

# current barcode
curr_barcode = []

# let user know they may take readings
display.text_pixels("Ready!",font=my_font)
display.update()

# read in the bar code
while(len(curr_barcode) < 4):
    if(buttons.enter == True):
        if(sensor.color == 1):
            curr_barcode.append(1)
        else:
            curr_barcode.append(0)
        string = str(sensor.color) + " was read. \n" + str(4 - len(curr_barcode)) + " readings left."
        display.text_pixels(string,font=my_font)
        display.update()
        time.sleep(0.3)

# barcode lists
BARCODE_TYPE_ONE = [1, 0, 0, 0]
BARCODE_TYPE_TWO = [1, 0, 1, 0]
BARCODE_TYPE_THREE = [1, 1, 0, 0]
BARCODE_TYPE_FOUR = [1,0,0,1]

# list of barcodes
BARCODES = [BARCODE_TYPE_ONE, BARCODE_TYPE_TWO, BARCODE_TYPE_THREE, BARCODE_TYPE_FOUR]

# check each barcode to see if it matches the current barcode
for i in range(len(BARCODES)):
    if(curr_barcode == BARCODES[i]):
        string = str(curr_barcode) + "\nType " + str(i+1)
        display.text_pixels(string,font=my_font)
        display.update()
        break
    else:
        display.text_pixels("None",font=my_font)
        display.update()