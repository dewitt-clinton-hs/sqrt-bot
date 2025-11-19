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

class Bot: # Make a blueprint for a robot
    def __init__(self):
        self.left_wheel = Motor(Ports.PORT1) # Connect to the motor at port 1 (controlling the left wheel)
        self.right_wheel = Motor(Ports.PORT2) # Connect to the motor at port 2 (controlling the right wheel)

        self.conveyor = Motor(Ports.PORT3) # Connect to the motor at port 3 (controlling the conveyor belt)
        self.intake = Motor(Ports.PORT4) # Connect to the motor at port 4 (controlling the intake)
        self.intake_button = Bumper(brain.three_wire_port.d) # Connect to the button on port D of the three wire port

    def f(self, pos): return int(pos**2 * 0.01 + pos) # Function to convert stick position to an appropriate RPM (0.01x^2 + x)

    def drive(self, pos):
        self.left_wheel.spin(FORWARD, self.f(pos))
        self.right_wheel.spin(FORWARD, self.f(pos) * -1) # Turn at the same speed but reverse the direction

    def turn(self, pos):
        self.left_wheel.spin(FORWARD, self.f(pos))
        self.right_wheel.spin(FORWARD, self.f(pos))

    def stop(self):
        self.left_wheel.stop()
        self.right_wheel.stop()

sqrt_bot = Bot() # Create an instance of SqrtBot, which represents the robot

controller.axis3.changed(sqrt_bot.drive(), controller.axis3.position())
controller.axis1.changed(sqrt_bot.turn(), controller.axis1.position())
