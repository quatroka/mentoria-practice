""" File to execute Pset 2 """
from Robot import Robot

print("""===============
Move Foward: F
Move Left: L
Move Right: R
Move Back: B
===============
Insert the sequence of moves: """)

ROBOT = Robot()
ROBOT.read_and_execute_movement(input())
print('\nFinal state: {0} {1} {2}'.format(ROBOT.get_x(), ROBOT.get_y(), ROBOT.get_face()))
