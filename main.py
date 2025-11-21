# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       student                                                      #
# 	Created:      11/3/2025, 3:03:12 PM                                        #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

brain = Brain()
controller = Controller()

# Motor connections via port
left_wheel = Motor(Ports.PORT1) # Connect to the motor at port 1 (controlling the left wheel)
right_wheel = Motor(Ports.PORT2) # Connect to the motor at port 2 (controlling the right wheel)
conveyor = Motor(Ports.PORT3) # Connect to the motor at port 3 (controlling the conveyor belt)
intake = Motor(Ports.PORT4) # Connect to the motor at port 4 (controlling the intake) 

# Note: The right wheel's direction is the reverse of the left wheel. So FORWARD for the left wheel is REVERSE for the right wheel and vice versa.
def drive(pos):
    left_wheel.spin(FORWARD, pos * 2.5)
    right_wheel.spin(FORWARD, pos * -2.5)

def turn(pos):
    left_wheel.spin(FORWARD, pos * 2.5)
    right_wheel.spin(FORWARD, pos * 2.5)

def stop():
    left_wheel.stop()
    right_wheel.stop()

while True: # Infinite loop

    if controller.axis1.position() > 0: turn(controller.axis1.position())
    elif controller.axis1.position() < 0: turn(controller.axis1.position())
    elif controller.axis3.position() > 0: drive(controller.axis3.position())
    elif controller.axis3.position() < 0: drive(controller.axis3.position())
    else: stop()

    if controller.buttonR1.pressing(): conveyor.spin(FORWARD, 100)
    elif controller.buttonL1.pressing(): conveyor.spin(REVERSE, 100)
    else: conveyor.stop()

    controls = { # Collection of all the joystick directions and their corresponding position
        "right_x": controller.axis1.position(),
        "right_y": controller.axis2.position(),
        "left_y": controller.axis3.position(),
        "left_x": controller.axis4.position()
    }

    for i in controls: # Error logging
        if controls[i] > 10 or controls[i] < -10: # If position changed

            # Print position
            brain.screen.print(i + " = " + str(controls[i]))
            brain.screen.new_line()
            brain.screen.clear_screen()
