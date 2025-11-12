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

    def drive(self, direction, speed):
        self.left_wheel.spin(direction, speed)
        self.right_wheel.spin(direction, speed * -1) # Turn at the same speed but reverse the direction

    def turn(self, direction, speed):
        self.left_wheel.spin(direction, speed)
        self.right_wheel.spin(direction, speed)

    def stop(self):
        self.left_wheel.stop()
        self.right_wheel.stop()

class BotController:
    def __init__(self):
        self.left_x = controller.axis1 # Axis 1 of the controller is the left-right movement of the right joystick
        self.left_y = controller.axis2 # Axis 2 of the controller is the up-down movement of the right joystick

        self.right_x = controller.axis3 # Axis 3 of the controller is the up-down movement of the left joystick
        self.right_y = controller.axis4 # Axis 4 of the controller is the left movement of the left joystick

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
    left_y, right_x = bot_controls["left_y"], bot_controls["right_x"] # Joysticks to go forward/back and left/right

    # Defining conditions with deadzones
    not_turning = right_x > -15 and right_x < 15
    not_driving = left_y > -15 and left_y < 15

    if not not_driving and not_turning: # If driving (not not driving) and not turning
        sqrt_bot.drive(FORWARD, left_y) # Drive at the [stick position]RPM (if negative, wheels go in reverse)
    else: sqrt_bot.stop() # In any other case, just stop the bot


    brain.screen.print("LEFT_Y: " + str(bot_controls["left_y"]))
    brain.screen.new_line()
    brain.screen.print("LEFT_X: " + str(bot_controls["left_x"]))
