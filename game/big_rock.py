import arcade
from game.constants import *
from game.point import *
from game.velocity import *
from game.flying_object import *
from game.ship import *
from game.rock import *
from game.medium_rock import *
from game.small_rock import *
from abc import abstractmethod

class BigRock(Rock):
    """Sets a BigRock class to represent the big space rocks."""
    def __init__(self):
        """Initializes values from parent class"""
        super().__init__()
        """Initializes as a point in a random position"""
        self.radius = BIG_ROCK_RADIUS
        self.hits_left = 1        
        self.texture = arcade.load_texture("./images/meteorGrey_big1.png")
        self.width = self.texture.width
        self.height = self.texture.height
        self.point_awarded = 1
        self.damage = 3
        self.spinning = BIG_ROCK_SPIN          
        
    
    def gotHit(self):        
        """When the rock is hit, its not alive anymore, and returns the points awarded. It also splits into two medium rocks and one small rock."""
        arcade.play_sound(self.sound)
        self.alive = False        
        medium_rock_1 = MediumRock(self.center.x, self.center.y, self.velocity.dx, self.velocity.dy + 2)
        medium_rock_2 = MediumRock(self.center.x, self.center.y, self.velocity.dx, self.velocity.dy - 2)
        small_rock_1 = SmallRock(self.center.x, self.center.y, self.velocity.dx + 5, self.velocity.dy)
        rock_list = [medium_rock_1, medium_rock_2, small_rock_1]
        return rock_list

    def award(self):
        """Return points awarded"""
        return self.point_awarded