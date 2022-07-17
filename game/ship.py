from game.bullet import *

class Ship(FlyingObject):
    """Sets a Spaceship class to represent the spaceship."""
    def __init__(self):
        """Initializes values from parent class"""
        super().__init__()
        """Initializes as a point in the center of the screen"""        
        self.center.x = SCREEN_WIDTH // 2
        self.center.y = SCREEN_HEIGHT // 2
        self.angle = 0                
        self.radius = SHIP_RADIUS
        self.lives = 100
        self.alive = True
        self.texture = arcade.load_texture("./images/playerShip1_orange.png")
        self.width = self.texture.width // 2
        self.height = self.texture.height // 2
        self.hitsound = arcade.load_sound("./sounds/shipcollision.wav")        
    
    def left_arrow(self):
        """ Turn the ship to the left """        
        self.velocity.dx -= .25

    def right_arrow(self):
        """ Turn the ship to the right """        
        self.velocity.dx += .25
    
    def up_arrow(self):
        """ Thrust forward """                
        self.velocity.dy += .25

    def down_arrow(self):
        """ Thrust backward """        
        self.velocity.dy -= .25

    def gotHit(self):
        """The ships makes sound when hit by lasers or rocks"""
        arcade.play_sound(self.hitsound)
        
    
    def laser(self):
        """Creates a laser bullet taking into consideration the ship's angle, position and velocity"""
        bullet = Bullet(self.angle + 90, self.center.x, self.center.y, self.velocity.dx, self.velocity.dy)        
        bullet.fire()
        return bullet