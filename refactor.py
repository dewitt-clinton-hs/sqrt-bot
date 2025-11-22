# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       Arymus Reyes & Camila Rodriguez                              #
# 	Created:      11/3/2025, 3:03:12 PM                                        #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# This code is refactored to be more readable. It has yet to be tested.

# Library imports
from vex import *

brain = Brain()
controller = Controller()

class SqrtBot:
    def __init__(self):

        # Port connections
        self.left_wheel = Motor(Ports.PORT1)
        self.right_wheel = Motor(Ports.PORT2, True) # The second argument reverses the direction of the right wheel, undoing its naturally reversed state.

        self.conveyor = Motor(Ports.PORT3)
        self.intake = Motor(Ports.PORT4)

        self.drive_train = DriveTrain(self.left_wheel, self.right_wheel)
        self.pick_up = MotorGroup(self.intake, self.conveyor)

    def autonomous(self): self.drive_train.drive_for(FORWARD, 12, INCHES) # The autonomous code, drive 12 inches forward

    def driver(self): # Manual code (controlled with controller)

        # Note: The right wheel's direction is the reverse of the left wheel. So FORWARD for the left wheel is REVERSE for the right wheel and vice versa.
        while True:
        
            # If the left-right positioning of the right joystick (controller.axis1) is outside the range 7 to -7
            if controller.axis1.position() > 7 or controller.axis1.position() < -7:

                # Multiply the joystick position by 3 to get a fast RPM and drive the robot forward at that speed
                self.left_wheel.spin(FORWARD, controller.axis1.position() * 3)
                self.right_wheel.spin(REVERSE, controller.axis1.position() * 3) # Remember, the FORWARD for the right

            # If the up-down positioning of the left joystick is outside the range of 7 to -7
            elif controller.axis3.position() > 7 or controller.axis3.position() < -7:

                # Multiply the joystick position by 3 to get a fast RPM and drive the robot forward at that speed
                self.left_wheel.spin(FORWARD, controller.axis3.position() * 3)
                self.right_wheel.spin(FORWARD, controller.axis3.position() * 3)

            else:

                # Stop the robot
                self.left_wheel.stop()
                self.right_wheel.stop()

            # Binds for buttons R1, L1, B, and A
            if controller.buttonR1.pressing(): self.conveyor.spin(FORWARD, 200)
            elif controller.buttonL1.pressing(): self.conveyor.spin(REVERSE, 200)
            else: self.conveyor.stop()
            
            if controller.buttonB.pressing(): self.intake.spin(FORWARD, 200)
            elif controller.buttonA.pressing(): self.intake.spin(REVERSE, 200)
            else: self.intake.stop()

sqrt_bot = SqrtBot() # Create an instance of SqrtBot
competition = Competition(sqrt_bot.driver, sqrt_bot.autonomous) # Initialize a competition instance with the two functions
