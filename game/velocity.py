class Velocity:    
    """Creates a Velocity class to set flying objects movement speed"""
    def __init__(self):
        """Sets speed to zero on both x and y-axis (float numbers)"""
        self.dx = 0.0
        self.dy = 0.0

    @property
    def getDX(self):
        """return dx value"""
        return self.__dx
    
    @getDX.setter
    def setDX(self, dx_value):
        """Defines dx value"""
        if dx_value < 0:
            self.__dx = 0
        elif dx_value > .25:
            self.__dx = .25 #sets speed limit at .25
        else:
            self.__dx = dx_value

    @property
    def getDY(self):
        """Return dy value"""
        return self.__dy
    
    @getDY.setter
    def setDY(self, dy_value):
        """Defines dy value"""
        if dy_value < 0:
            self.__dy = 0
        elif dy_value > .25:
            self.__dy = .25 #sets speed limit at .25
        else:
            self.__dy = dy_value