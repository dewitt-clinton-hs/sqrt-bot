# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       Arymus Reyes & Camila Rodriguez                                                      #
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
intake = Motor(Ports.PORT4, True) # Connect to the motor at port 4 (controlling the intake) and reverse the direction

drive_train = DriveTrain(left_wheel, right_wheel)
pick_up = MotorGroup(intake, conveyor)

def autonomous(): # Autonomous code
    drive_train.drive_for(FORWARD, 12, INCHES)

def driver(): # Manual code

    # Note: The right wheel's direction is the reverse of the left wheel. So FORWARD for the left wheel is REVERSE for the right wheel and vice versa.
    while True:
        if controller.axis1.position() > 0 or controller.axis1.position() < 0:
            left_wheel.spin(FORWARD, controller.axis1.position() * 3)
            right_wheel.spin(FORWARD, controller.axis1.position() * 3)

        elif controller.axis3.position() > 0 or controller.axis3.position():
            left_wheel.spin(FORWARD, controller.axis3.position() * 3)
            right_wheel.spin(FORWARD, controller.axis3.position() * -3)

        else:
            left_wheel.stop()
            right_wheel.stop()

        if controller.buttonR1.pressing(): conveyor.spin(FORWARD, 200)
        elif controller.buttonL1.pressing(): conveyor.spin(REVERSE, 200)
        else: conveyor.stop()
        
        if controller.buttonB.pressing(): intake.spin(FORWARD, 200)
        elif controller.buttonA.pressing(): intake.spin(REVERSE, 200)
        else: intake.stop()

competition = Competition(driver, autonomous)
