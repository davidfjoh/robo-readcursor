# robo-readcursor
utility to help find pixel colors when creating pyrobot scripts

Often when developing pyrobot scripts it is necessary to wait for the next screen before invoking the next button press.
This can be done with the following code:

import pyrobot
robot = pyrobot.Robot()

def waitForColor(location, color):
    trys = 0
    while robot.get_pixel(x = location[0], y = location[1]) != color:
        robot.sleep(.2)
        trys = trys + 1
        if trys > 100:
            print "Wait for Color timeout:"
            print "Looking For ", location, color 
            print "found ", location, robot.get_pixel(x = location[0], y = location[1])
            trys = 0
  
  robot.move_and_click(200, 95,'Left')  # press some button
  waitForColor((796, 328),(204, 204, 153))  # wait for new screen that results from the button press

However it can be tedious to find the exact position and color of some unique pixel on the screen the indicates the new screen is displayed, and it can be tedious to find the location of the button to begin with.

readCursor.py is a simple UI wrapping get_mouse_pos() and get_pixel() that allows you to see the position and pixel color of the cursor as you move it around the screen.  It uses Tkinter as the UI framework so that it does not require a special graphics module to be installed to use.  The location, pixel color pair is stored in an editable text field so that it can be selected and copied for pasting into the pyRobot script being developed.

To use invoke 'python readCursor.py' from a command prompt, and a small window will pop-up showing the current cursor location and pixel value as two tuples.

When pointing over a button to press just copy the contents of the first tuple (the cursor screen location)
When pointing over a pixel to check copy the entire pair of tuples.
