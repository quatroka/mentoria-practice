""" Pset 2 Robot class file """
class Robot():
    """ Class for the object Robot """
    def __init__(self):
        self.__x = 0
        self.__y = 0
        self.__face = 'N'

    def read_and_execute_movement(self, moves):
        """ Read a sequence of characters and execute the
            respective movements """
        print('\nInitial state: 0 0 N\n')
        for move in moves.upper():
            if move == 'F':
                self.__move_forward()
            elif move == 'R':
                self.__move_right()
            else:
                self.__move_left()
            print('Moving to: {0} {1} {2}'.format(self.get_x(), self.get_y(), self.get_face()))

    def __move_forward(self):
        """ Move the robot to foward """
        if self.__face == 'N':
            self.__y += 1
        elif self.__face == 'E':
            self.__x += 1
        elif self.__face == 'S':
            self.__y -= 1
        else:
            self.__x -= 1

    def __move_right(self):
        """ Rotate the robot to right """
        if self.__face == 'N':
            self.__face = 'E'
        elif self.__face == 'E':
            self.__face = 'S'
        elif self.__face == 'S':
            self.__face = 'O'
        else:
            self.__face = 'N'

    def __move_left(self):
        """ Rotate the robot to right """
        if self.__face == 'N':
            self.__face = 'O'
        elif self.__face == 'E':
            self.__face = 'N'
        elif self.__face == 'S':
            self.__face = 'E'
        else:
            self.__face = 'S'

    def get_x(self):
        """ Return x position of robot """
        return self.__x

    def get_y(self):
        """ Return y position of robot """
        return self.__y

    def get_face(self):
        """ Return face sense of robot """
        return self.__face
