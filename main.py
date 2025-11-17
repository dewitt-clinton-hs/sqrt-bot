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

bot_controls = { # Dictionary containing all of the control names and their starting position (0)
    "right_x": 0,
    "right_y": 0,
    "left_y": 0,
    "left_x": 0
}

# A class is a blueprint for an object, the object being a robot
class Bot:
    def __init__(self):
        self.left_wheel = Motor(Ports.PORT1) # Connect to the motor at port 1 (controlling the left wheel)
        self.right_wheel = Motor(Ports.PORT2) # Connect to the motor at port 2 (controlling the right wheel)

        self.conveyor = Motor(Ports.PORT3) # Connect to the motor at port 3 (controlling the conveyor belt)
        self.intake = Motor(Ports.PORT4) # Connect to the motor at port 4 (controlling the intake)
        self.intake_button = Bumper(brain.three_wire_port.d) # Connect to the button on port D of the three wire port

    def f(self, pos): return (pos**2 * 0.01) + pos # Function to convert stick position to an appropriate RPM (0.01x^2 + x)

    def drive(self, pos):
        self.left_wheel.spin(FORWARD, self.f(pos))
        self.right_wheel.spin(FORWARD, self.f(pos) * -1) # Turn at the same speed but reverse the direction

    def turn(self, pos):
        self.left_wheel.spin(FORWARD, self.f(pos))
        self.right_wheel.spin(FORWARD, self.f(pos))

    def stop(self):
        self.left_wheel.stop()
        self.right_wheel.stop()

class BotController:
    def __init__(self):
        self.right_y = controller.axis1 # Axis 1 of the controller is the left-right movement of the right joystick
        self.right_x = controller.axis2 # Axis 2 of the controller is the up-down movement of the right joystick

        self.left_x = controller.axis3 # Axis 3 of the controller is the up-down movement of the left joystick
        self.left_y = controller.axis4 # Axis 4 of the controller is the left movement of the left joystick

        self.controls = [self.right_x, self.right_y, self.left_y, self.left_x] # List containing the controls

    def update_controls(self):
        global bot_controls # Define the controls as globally-scoped variables so the rest of the code can access them

        x = 0 # Represents the index of the controls list
        for i in bot_controls:
            bot_controls[i] = self.controls[x].position() # Set the key of bot_controls with the position of the corresponding control
            x += 1 # Increment the index by 1 for the next loop

sqrt_bot = Bot() # Create an instance of SqrtBot, which represents the robot
sqrt_controller = BotController() # Create an instance of BotController, which represents the controller we use to drive sqrt_bot

while True:
    sqrt_controller.update_controls() # Constantly update the positions of the joysticks

    # Controls
    right_x = bot_controls["right_x"]
    right_y = bot_controls["right_y"]
    left_y = bot_controls["left_y"]
    left_x = bot_controls["left_x"]

    # Defining conditions with deadzones (stop if the joystick position is above -7 and below 7)
    driving = right_y < -7 or right_y > 7
    turning = left_x < -7 or left_x > 7

    if turning: sqrt_bot.turn(left_x)
    elif driving: sqrt_bot.drive(right_y)
    else: sqrt_bot.stop()
