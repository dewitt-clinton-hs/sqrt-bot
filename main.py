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

def update_controls():
        global bot_controls # Define the controls as globally-scoped variables so the rest of the code can access them
        
        # Defining all of the controls based on their axes
        right_x = controller.axis1
        right_y = controller.axis2
        left_y = controller.axis3
        left_x = controller.axis4
        
        controls = [right_x, right_y, left_y, left_x] # A list of all the controls

        x = 0 # Represents the index of the controls list
        for i in bot_controls:
            bot_controls[i] = controls[x].position() # Set the key of bot_controls with the position of the corresponding control
            x += 1 # Increment the index by 1 for the next loop

sqrt_bot = Bot() # Create an instance of SqrtBot, which represents the robot

while True:
    update_controls() # Constantly update the positions of the joysticks

    # Define moving conditions with deadzones (joystick position above 10 or below -10)
    turning = bot_controls["right_x"] > 10 or bot_controls["right_x"] < -10
    driving = bot_controls["left_y"] > 10 or bot_controls["left_y"] < -10

    # Note: Movement functions take joystick position as their parameter, which are converted into RPM for the motors
    if turning: sqrt_bot.turn(bot_controls["right_x"])
    elif driving: sqrt_bot.drive(bot_controls["left_y"])
    else: sqrt_bot.stop()
