import arcade
import math
import random
from game.constants import *
from game.point import *
from game.velocity import *
from game.flying_object import *
from game.ship import *
from abc import abstractmethod

class Rock(FlyingObject):
    """Sets a Rock class to represent the space rocks."""
    def __init__(self):
        """Initializes values from parent class"""
        super().__init__()
        self.angle = random.randrange(0, 360)       
        self.center.x = random.randrange(1, SCREEN_WIDTH)
        self.center.y = random.randrange(500, SCREEN_HEIGHT)        
        self.alive = True
        self.speed = BIG_ROCK_SPEED        
        self.velocity.dx = math.cos(math.radians(self.angle)) * self.speed
        self.velocity.dy = math.sin(math.radians(self.angle)) * self.speed
        self.sound = arcade.load_sound("./sounds/hitsound.wav")
    
    def spin(self):
        """Spins the space rocks"""
        self.angle += self.spinning

    
    def hit(self):
        """Abstract method for when the rock hits the ship. It will be implemented on child classes"""
        arcade.play_sound(self.sound)
        return self.damage

    @abstractmethod
    def gotHit(self):
        """Abstract method to check if the rock got hit by a bullet. It will be implemented on child classes"""
        pass

    @abstractmethod
    def award(self):
        """Abstract method to return points awarded. It will be implemented on child classes"""
        pass