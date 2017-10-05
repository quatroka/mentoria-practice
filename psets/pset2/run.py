#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" File to execute Pset 2 """
from Robot import Robot

print("""===============
Move to Foward: F
Rotate to Left: L
Rotate to Right: R
===============
Insert the sequence of moves: """)

ROBOT = Robot()
ROBOT.read_and_execute_movement(input())
print('\nFinal state: {0} {1} {2}'.format(ROBOT.get_x(), ROBOT.get_y(), ROBOT.get_face()))
