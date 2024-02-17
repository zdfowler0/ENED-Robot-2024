### Robot Software Setup (Windows)
# 1. Install VS Code
Go to [VS Code](https://code.visualstudio.com/Download) and install the latest version.

# 2. Install Extensions
Go into VS Code. On the left side bar, there is a button with 4 square (Extensions tab) *(Shortcut: Ctrl + Shift + X)*.
Go into this tab and find the following extensions, and download them:
- Python (Extension ID (copy into extensions search bar if having trouble): ms-python.python)
- ev3dev-browser (ev3dev.ev3dev-browser)
- LEGO® MINDSTORMS® EV3 MicroPython (lego-education.ev3-micropython)
*Note Pylance (ms-python.vscode-pylance) may require a reload after installations*

# 3. Connecting the EV3 Brick to WiFi and (Bluetooth)
The easiest way I have found how to do this is to connect via Bluetooth. The [ev3dev website](https://www.ev3dev.org/docs/tutorials/connecting-to-the-internet-via-bluetooth/) has good documentation on this.
This took me a little while to get working but eventually the EV3 does connect. Once the EV3 is connected to the internet and Bluetooth, files can be uploaded.

# 4. Uploading files
## Selecting Files
- In VS Code once again, go to Explorer tab *(Shortcut: Ctrl + Shift + E)*. 
- Select the python file you would like to upload and open it by double clicking (You can access a folder by expolring the "File" menu, or using Ctrl + K then Ctrl + O. From there, find the folder where the file is stored.)
## Connecting to the EV3 in VS Code
- In the bottom corner of the Explorer pane, find the section labeled "EV3DEV DEVICE BROWSER"
- Press "Click here to connect to a device"
- If the EV3 pops up at the top, go ahead and select it. Otherwise (such as my case), select "I don't see my device"
### I don't see my device
- From here, make a name for the device *(ex: robot)* and then enter the ip address found at the top of the home screen on the EV3.
- Once the proper information is entered the EV3 will connect.
## Upload files
- Once the EV3 is connected, press the download button near the name of the device; this will copy the code onto the robot.

Hopefully this documentation helps with sending files to the EV3. Good luck!
