#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Pset 2 Robot class file """
class Robot():
    """ Class for the object Robot """
    def __init__(self):
        self.x = 0
        self.y = 0
        self.face = 1

    def read_and_execute_movement(self, moves):
        """ Read a sequence of characters and execute the
            respective movements """
        print('\nInitial state: 0 0 N\n')
        for move in moves.upper():
            if move == 'F':
                self.move_forward()
            elif move == 'R':
                self.move_right()
            else:
                self.move_left()
            

    def move_forward(self):
        """ Move the robot to foward """
        if self.face == 1:
            self.y += 1
        elif self.face == 2:
            self.x += 1
        elif self.face == 3:
            self.y -= 1
        elif self.face == 4:
            self.x -= 1
        print('Moving to: {0} {1}'.format(self.x, self.y))

    def move_right(self):
        """ Rotate the robot to right """
        if self.face == 4:
            self.face = 0
        self.face += 1

    def move_left(self):
        """ Rotate the robot to left """
        if self.face == 1:
            self.face = 5
        self.face -= 1
