import arcade
import math
import random
from game.constants import *
from game.point import *
from game.velocity import *
from game.flying_object import *
from game.ship import *
from game.rock import *
from game.big_rock import *
from game.small_rock import *
from abc import ABC
from abc import abstractmethod

class MediumRock(Rock):
    """Sets a MediumRock class to represent the medium space rocks."""
    def __init__(self, x, y, dx, dy):
        """Initializes values from parent class"""
        super().__init__()
        """Initializes as a point in the same position as the BigRock it came from"""
        self.center.x = x
        self.center.y = y
        self.velocity.dx = dx
        self.velocity.dy = dy
        self.radius = MEDIUM_ROCK_RADIUS
        self.hits_left = 1        
        self.texture = arcade.load_texture("./images/meteorGrey_med1.png")
        self.width = self.texture.width
        self.height = self.texture.height 
        self.point_awarded = 3          
        self.spinning = MEDIUM_ROCK_SPIN   
        self.damage = 2 
    
    
    
    def gotHit(self):        
        """When the rock is hit, its not alive anymore, and returns the points awarded. It also splits into two medium rocks and one small rock."""
        arcade.play_sound(self.sound)
        self.alive = False        
        small_rock_1 = SmallRock(self.center.x, self.center.y, self.velocity.dx + 1.5, self.velocity.dy + 1.5)
        small_rock_2 = SmallRock(self.center.x, self.center.y, self.velocity.dx - 1.5, self.velocity.dy - 1.5)
        
        rock_list = [small_rock_1, small_rock_2]
        return rock_list
    
    def award(self):
        """Return points awarded"""
        return self.point_awarded