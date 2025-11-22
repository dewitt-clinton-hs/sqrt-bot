
# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       camilarodriguez                                              #
# 	Created:      11/20/2025, 8:17:46 PM                                       #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()

brain.screen.print("Hello V5")


        
# VEXcode Generated Robot Configuration
import math
import random

# Brain should be defined by default
brain = Brain()
motorL=Motor(Ports.PORT1)#UPDATE PORTS
motorR=Motor(Ports.PORT10)
drivetrain=DriveTrain(motorL,motorR)

conveyor_motor = Motor(Ports.PORT3)
intake_motor =Motor(Ports.PORT4,True)
pick_up=MotorGroup(intake_motor,conveyor_motor)

# ----------------------------------------------------
# Project Code (auto)
# ----------------------------------------------------

def auto():
    drivetrain.turn_for(RIGHT,88,DEGREES)
    drivetrain.drive_for(FORWARD,27,INCHES)
    pick_up.spin_for(REVERSE,-600,DEGREES)#basically does it thing enough to hypothetically pick up 3 ball off the pole thing
    drivetrain.turn_for(LEFT,120,DEGREES)#42-44 ARE TURNS TO REACH THE BALLS THAT ARE LIKE IN A SQUARE SHAPE
    drivetrain.drive_for(FORWARD,27,INCHES)
    drivetrain.turn_for(LEFT,40,DEGREES)
    pick_up.spin_for(REVERSE,-90,DEGREES)#ATTEMPTS TO PICK UP RED BALL DIRECTLY INFRONT, MAY NOT WORK
    drivetrain.drive_for(FORWARD,2,INCHES)#MOVES FORWARD TO GET NEXT BALL
    pick_up.spin_for(REVERSE,-90,DEGREES)#ATTEMPTS TO PICK UP RED BALL DIRECTLY INFRONT, MAY NOT WORK
    drivetrain.drive_for(FORWARD,22,INCHES)#DRIVES TOWARD FLOOR GOAL
    pick_up.spin_for(FORWARD,1,TURNS)#SHOULD SHOOT OUT BALL FROM INSIDE ROBOT INTO FLOOR GOAL
auto()
