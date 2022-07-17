from game.big_rock import *

class Director(arcade.Window):
    """
    This class handles all the game callbacks and interaction.
    This class will then call the appropriate functions of
    each of the other classes.    
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)

        self.alive = True
        
        self.held_keys = set()

        self.background = arcade.load_texture("./images/nebula.jpg")

        self.ship = Ship()

        self.score = 0     

        self.bullets = []

        self.rocks = []          

        self.create_rocks()   

    def create_rocks(self):
        """Creates targets as rocks"""
        for i in range(INITIAL_ROCK_COUNT):
            rock = BigRock()
            self.rocks.append(rock)      

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """
        
        arcade.start_render()

        #Applies background texture
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.ship.draw()        
            
        for rock in self.rocks:
            rock.draw()              

        for bullet in self.bullets:
            bullet.draw()            

        self.draw_score()  

        self.draw_status()

        if self.ship.lives <= 0:            
            self.game_over()
            self.play_again()            
        
        if self.score == 320:            
            self.victory()
            self.play_again()

        if len(self.rocks) < 5:            
            self.create_rocks()

    def draw_score(self):
        """
        Puts the current score on the screen
        """
        score_text = "Score: {}".format(self.score)
        start_x = 10
        start_y = SCREEN_HEIGHT - 40
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=20, color=arcade.color.WHITE_SMOKE)

    def draw_status(self):
        """
        Puts the current status on the screen
        """
        status_text = "Status: {}%".format(self.ship.lives)
        start_x = SCREEN_WIDTH - 130
        start_y = SCREEN_HEIGHT - 40
        arcade.draw_text(status_text, start_x=start_x, start_y=start_y, font_size=20, color=arcade.color.YELLOW)

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_keys()

        self.ship.notWrapScreen()   
        
        for rock in self.rocks:
            rock.spin()
            rock.advance()
            rock.wrapScreen()            

        for bullet in self.bullets:
            bullet.advance()    
        
        self.ship.advance()        

        self.check_collisions()

    def check_collisions(self):
        """        
        Updates scores and removes dead items.
        :return:
        """
        
        """Checks to see if bullets have hit rocks. """
        for bullet in self.bullets:
            for rock in self.rocks:

                # Make sure they are both alive before checking for a collision
                if bullet.alive and rock.alive:
                    too_close = bullet.radius + rock.radius

                    if (abs(bullet.center.x - rock.center.x) < too_close and
                                abs(bullet.center.y - rock.center.y) < too_close):
                        # its a hit!
                        bullet.alive = False
                        rock_list = rock.gotHit()
                        self.rocks += rock_list
                        self.score += rock.award()
        
        """Checks if rocks have hit the ship."""
        for rock in self.rocks:   
            
            # Make sure they are both alive before checking for a collision
            if rock.alive and self.ship.alive:
                too_close = rock.radius + self.ship.radius
                
                if (abs(self.ship.center.x - rock.center.x) < too_close and
                            abs(self.ship.center.y - rock.center.y) < too_close):
                    # its a hit!
                    self.ship.gotHit()                                                                                                    
                    self.ship.lives -= rock.hit()                    

        """Checks if bullets have hit the ship."""
        for bullet in self.bullets:   
            """Only bullets fired more than 30 frames ago will hit the ship"""
            # Make sure they are both alive before checking for a collision
            if bullet.alive and bullet.lifespan < 30 and self.ship.alive:
                too_close = bullet.radius + self.ship.radius
                
                if (abs(self.ship.center.x - bullet.center.x) < too_close and
                            abs(self.ship.center.y - bullet.center.y) < too_close):
                    # its a hit!                                                                                                    
                    self.ship.gotHit()
                    self.ship.lives -= bullet.hit()                    
                        # We will wait to remove the dead objects until after we
                        # finish going through the list
        
        """Checks if the ship is still alive"""
        if self.ship.lives <= 0:
            self.ship.alive = False            

        # Now, check for anything that is dead, and remove it
        self.cleanup_zombies()

    def cleanup_zombies(self):
        """
        Removes any dead bullets or targets from the list.
        :return:
        """
        for bullet in self.bullets:            
            bullet.is_alive()
            if bullet.alive == False:
                self.bullets.remove(bullet)        

        for rock in self.rocks:
            if not rock.alive:
                self.rocks.remove(rock)         

    def check_keys(self):
        """
        This function checks for keys that are being held down.
        You will need to put your own method calls in here.
        """        

        if arcade.key.LEFT in self.held_keys:
            self.ship.left_arrow()

        if arcade.key.RIGHT in self.held_keys:
            self.ship.right_arrow()

        if arcade.key.UP in self.held_keys:
            self.ship.up_arrow()

        if arcade.key.DOWN in self.held_keys:
            self.ship.down_arrow()

        if arcade.key.SPACE in self.held_keys:            
            bullet = self.ship.laser()
            self.bullets.append(bullet)
            self.held_keys.remove(arcade.key.SPACE)

    def on_key_press(self, key, modifiers):
        """
        Puts the current key in the set of keys that are being held.        
        """
        if self.ship.alive:
            self.held_keys.add(key)   

        if self.alive == False and key == arcade.key.Y:
            self.restart()
        elif self.alive == False and key == arcade.key.N:
            arcade.close_window()    

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)                  

    def game_over(self):
        """When lives run out, the game is over"""
        game_over_message = "Game Over"
        game_over_message_x = 0
        game_over_message_y = SCREEN_HEIGHT // 2
        arcade.draw_text(game_over_message, start_x=game_over_message_x, start_y=game_over_message_y, font_size=80, color=arcade.color.WHITE, width=SCREEN_WIDTH, align="center")

    def victory(self):
        """When all rocks are destroyed, it's victory"""
        victory_message = "Victory!"
        victory_message_x = 0
        victory_message_y = SCREEN_HEIGHT // 2
        arcade.draw_text(victory_message, start_x=victory_message_x, start_y=victory_message_y, font_size=80, color=arcade.color.WHITE, width=SCREEN_WIDTH, align="center")

    def play_again(self):
        """Asks plays if they want to play again"""
        self.alive = False
        play_again_message = "Want to play again? (Press Y or N)"
        play_again_message_x = 0
        play_again_message_y = SCREEN_HEIGHT // 2 - 100
        arcade.draw_text(play_again_message, start_x=play_again_message_x, start_y=play_again_message_y, font_size=30, color=arcade.color.WHITE, width=SCREEN_WIDTH, align="center")
        
    def restart(self):
        """Restarts the game on pressing Y"""
        
        self.alive = True        
        self.held_keys = set()
        self.background = arcade.load_texture("./background/nebula.jpg") #This is one of my above and beyond functionality. I decided to include a space picture as background instead of a black background.
        self.ship = Ship()
        self.score = 0     
        self.bullets = []
        self.rocks = []  
        self.create_rocks()