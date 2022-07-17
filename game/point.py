from game.constants import *

class Point:
    """Creates a Point class to represent the location of flying objects"""
    def __init__(self):
        """Initializes point at 0.0/0.0 (float numbers)"""
        self.x = 0.0
        self.y = 0.0
    
    @property
    def getX(self):
        """return x value"""
        return self.__x
    
    @getX.setter
    def setX(self, x_value):
        """Defines x value"""
        if x_value < 0:
            self.__x = 0
        elif x_value > SCREEN_WIDTH:
            self.__x = SCREEN_WIDTH
        else:
            self.__x = x_value

    @property
    def getY(self):
        """Return y value"""
        return self.__y
    
    @getY.setter
    def setY(self, y_value):
        """Defines y value"""
        if self.x_value < 0:
            self.__y = 0
        elif self.x_value > SCREEN_HEIGHT:
            self.__y = SCREEN_HEIGHT
        else:
            self.__y = y_value