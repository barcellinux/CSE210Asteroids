
import arcade
from abc import ABC
from game.constants import *
from game.point import *
from game.velocity import *

class FlyingObject(ABC):
    """Sets a FlyingObject class to represent commmon characteristics shared by ship, bullets and rocks."""
    def __init__(self):
        """Initializes the flying object as a point, sets its speed, and defines its status as alive"""
        self.center = Point()        
        self.velocity = Velocity()
        self.alive = True
        self.angle = 0      
        self.alpha = 255    

    @property
    def getAngle(self):
        """Return angle value"""
        return self.angle

    @getAngle.setter
    def setAngle(self, angle_value):
        """Defines angle value"""
        if angle_value < 0:
            self.angle = 0
        elif angle_value > 360:
            self.angle = 360
        else:
            self.angle = angle_value    
 
    def advance(self):
        """Moves the flying object by increasing its point coordinates by the velocity"""
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy
    
    def draw(self):
        """Draws the FlyingObject as a rectangle with texture"""
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.width, self.height, self.texture, self.angle, self.alpha)

    def wrapScreen(self):
        """If the flying object goes off-screen, it will reappear on the other side of the screen"""
        if self.center.x - self.width//2 > SCREEN_WIDTH:
            self.center.x = 0
        
        if self.center.x + self.width//2 < 0:
            self.center.x = SCREEN_WIDTH

        if self.center.y - self.height//2 > SCREEN_HEIGHT:
            self.center.y = 0
        
        if self.center.y + self.height//2 < 0:
            self.center.y = SCREEN_HEIGHT

    def notWrapScreen(self):
        """If the flying object goes off-screen, it won't reappear on the other side of the screen"""
        if self.center.x + self.width//2 > SCREEN_WIDTH:
            self.center.x = SCREEN_WIDTH - self.width//2
            self.velocity.dx = 0
            self.velocity.dy = 0
        
        if self.center.x - self.width//2 < 0:
            self.center.x = 0 + self.width//2
            self.velocity.dx = 0
            self.velocity.dy = 0

        if self.center.y + self.height//2 > SCREEN_HEIGHT:
            self.center.y = SCREEN_HEIGHT - self.height//2
            self.velocity.dx = 0
            self.velocity.dy = 0
        
        if self.center.y - self.height//2 < 0:
            self.center.y = 0 + self.height//2
            self.velocity.dx = 0
            self.velocity.dy = 0