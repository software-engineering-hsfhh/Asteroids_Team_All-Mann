"""
Asteroid Smasher

Shoot space rocks in this demo program created with
Python and the Arcade library.

Artwork from http://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.asteroid_smasher
"""
import random
import math
import arcade
import os

"""Julius"""
"""Lea"""
"""Laura"""
"""Merle"""
"""Merle"""
""Annika""


from typing import cast

STARTING_ASTEROID_COUNT = 3
SCALE = 0.5
OFFSCREEN_SPACE = 300
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Asteroid Smasher"
LEFT_LIMIT = -OFFSCREEN_SPACE
RIGHT_LIMIT = SCREEN_WIDTH + OFFSCREEN_SPACE
BOTTOM_LIMIT = -OFFSCREEN_SPACE
TOP_LIMIT = SCREEN_HEIGHT + OFFSCREEN_SPACE


class TurningSprite(arcade.Sprite):
    """ Sprite that sets its angle to the direction it is traveling in. """
    def update(self):
        """ Move the sprite """
        super().update()
        self.angle = math.degrees(math.atan2(self.change_y, self.change_x))


class ShipSprite(arcade.Sprite):
    """
    Sprite that represents our space ship.

    Derives from arcade.Sprite.
    """
    def __init__(self, filename, scale):
        """ Set up the space ship. """

        # Call the parent Sprite constructor
        super().__init__(filename, scale)

        # Info on where we are going.
        # Angle comes in automatically from the parent class.
        self.thrust = 0
        self.speed = 0
        self.max_speed = 4
        self.drag = 0.05
        self.respawning = 0

        # Mark that we are respawning.
        self.respawn()

    def respawn(self):
        """
        Called when we die and need to make a new ship.
        'respawning' is an invulnerability timer.
        """
        # If we are in the middle of respawning, this is non-zero.
        self.respawning = 1
        self.center_x = SCREEN_WIDTH / 2
        self.center_y = SCREEN_HEIGHT / 2
        self.angle = 0

    def update(self):
        """
        Update our position and other particulars.
        """
        if self.respawning:
            self.respawning += 1
            self.alpha = self.respawning
            if self.respawning > 250:
                self.respawning = 0
                self.alpha = 255
        if self.speed > 0:
            self.speed -= self.drag
            if self.speed < 0:
                self.speed = 0

        if self.speed < 0:
            self.speed += self.drag
            if self.speed > 0:
                self.speed = 0

        self.speed += self.thrust
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        if self.speed < -self.max_speed:
            self.speed = -self.max_speed

        self.change_x = -math.sin(math.radians(self.angle)) * self.speed
        self.change_y = math.cos(math.radians(self.angle)) * self.speed

        self.center_x += self.change_x
        self.center_y += self.change_y

        # If the ship goes off-screen, move it to the other side of the window
        if self.right < 0:
            self.left = SCREEN_WIDTH

        if self.left > SCREEN_WIDTH:
            self.right = 0

        if self.bottom < 0:
            self.top = SCREEN_HEIGHT

        if self.top > SCREEN_HEIGHT:
            self.bottom = 0

        """ Call the parent class. """
        super().update()


class AsteroidSprite(arcade.Sprite):
    """ Sprite that represents an asteroid. """

    def __init__(self, image_file_name, scale):
        super().__init__(image_file_name, scale=scale)
        self.size = 0

    def update(self):
        """ Move the asteroid around. """
        super().update()
        if self.center_x < LEFT_LIMIT:
            self.center_x = RIGHT_LIMIT
        if self.center_x > RIGHT_LIMIT:
            self.center_x = LEFT_LIMIT
        if self.center_y > TOP_LIMIT:
            self.center_y = BOTTOM_LIMIT
        if self.center_y < BOTTOM_LIMIT:
            self.center_y = TOP_LIMIT


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.frame_count = 0

        self.game_over = False

        # Sprite lists
        self.player_sprite_list = arcade.SpriteList()
        self.asteroid_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        # Set up the player
        self.score = 0
        self.player_sprite = None
        self.lives = 0

        # Sounds
        # TODO: load sounds

    def start_new_game(self):
        """ Set up the game and initialize the variables. """

        self.frame_count = 0
        self.game_over = False

        # Sprite lists
        self.player_sprite_list = arcade.SpriteList()
        self.asteroid_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        # Set up the player
        self.score = 0
        self.player_sprite = ShipSprite(":resources:images/space_shooter/playerShip1_orange.png", SCALE)
        self.player_sprite_list.append(self.player_sprite)
        self.lives = 0

        # ToDo: Set up the little icons that represent the player lives.

        # Make the asteroids
        image_list = (":resources:images/space_shooter/meteorGrey_big1.png",
                      ":resources:images/space_shooter/meteorGrey_big2.png",
                      ":resources:images/space_shooter/meteorGrey_big3.png",
                      ":resources:images/space_shooter/meteorGrey_big4.png")
        for i in range(STARTING_ASTEROID_COUNT):
            image_no = random.randrange(4)
            enemy_sprite = AsteroidSprite(image_list[image_no], SCALE)
            enemy_sprite.guid = "Asteroid"

            enemy_sprite.center_y = random.randrange(BOTTOM_LIMIT, TOP_LIMIT)
            enemy_sprite.center_x = random.randrange(LEFT_LIMIT, RIGHT_LIMIT)

            enemy_sprite.change_x = random.random() * 2 - 1
            enemy_sprite.change_y = random.random() * 2 - 1

            enemy_sprite.change_angle = (random.random() - 0.5) * 2
            enemy_sprite.size = 4
            self.asteroid_list.append(enemy_sprite)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.asteroid_list.draw()
        self.bullet_list.draw()
        self.player_sprite_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 70, arcade.color.WHITE, 13)

        output = f"Asteroid Count: {len(self.asteroid_list)}"
        arcade.draw_text(output, 10, 50, arcade.color.WHITE, 13)

    def on_key_press(self, symbol, modifiers):
        """ Called whenever a key is pressed. """
        if not self.player_sprite.respawning and symbol == arcade.key.SPACE:
            # TODO: # Shoot if the player hit the space bar and we aren't respawning.
            pass

        if symbol == arcade.key.LEFT:
            self.player_sprite.change_angle = 3
        elif symbol == arcade.key.RIGHT:
            self.player_sprite.change_angle = -3
        elif symbol == arcade.key.UP:
            self.player_sprite.thrust = 0.15
        elif symbol == arcade.key.DOWN:
            self.player_sprite.thrust = -.2

    def on_key_release(self, symbol, modifiers):
        """ Called whenever a key is released. """
        if symbol == arcade.key.LEFT:
            self.player_sprite.change_angle = 0
        elif symbol == arcade.key.RIGHT:
            self.player_sprite.change_angle = 0
        elif symbol == arcade.key.UP:
            self.player_sprite.thrust = 0
        elif symbol == arcade.key.DOWN:
            self.player_sprite.thrust = 0

    def split_asteroid(self, asteroid: AsteroidSprite):
        """ Split an asteroid into chunks. """
        x = asteroid.center_x
        y = asteroid.center_y
        self.score += 1

        if asteroid.size == 4:
            for i in range(3):
                image_no = random.randrange(2)
                image_list = [":resources:images/space_shooter/meteorGrey_med1.png",
                              ":resources:images/space_shooter/meteorGrey_med2.png"]

                enemy_sprite = AsteroidSprite(image_list[image_no],
                                              SCALE * 1.5)

                enemy_sprite.center_y = y
                enemy_sprite.center_x = x

                enemy_sprite.change_x = random.random() * 2.5 - 1.25
                enemy_sprite.change_y = random.random() * 2.5 - 1.25

                enemy_sprite.change_angle = (random.random() - 0.5) * 2
                enemy_sprite.size = 3

                self.asteroid_list.append(enemy_sprite)

        elif asteroid.size == 3:
            for i in range(3):
                image_no = random.randrange(2)
                image_list = [":resources:images/space_shooter/meteorGrey_small1.png",
                              ":resources:images/space_shooter/meteorGrey_small2.png"]

                enemy_sprite = AsteroidSprite(image_list[image_no],
                                              SCALE * 1.5)

                enemy_sprite.center_y = y
                enemy_sprite.center_x = x

                enemy_sprite.change_x = random.random() * 3 - 1.5
                enemy_sprite.change_y = random.random() * 3 - 1.5

                enemy_sprite.change_angle = (random.random() - 0.5) * 2
                enemy_sprite.size = 2

                self.asteroid_list.append(enemy_sprite)

        elif asteroid.size == 2:
            for i in range(3):
                image_no = random.randrange(2)
                image_list = [":resources:images/space_shooter/meteorGrey_tiny1.png",
                              ":resources:images/space_shooter/meteorGrey_tiny2.png"]

                enemy_sprite = AsteroidSprite(image_list[image_no],
                                              SCALE * 1.5)

                enemy_sprite.center_y = y
                enemy_sprite.center_x = x

                enemy_sprite.change_x = random.random() * 3.5 - 1.75
                enemy_sprite.change_y = random.random() * 3.5 - 1.75

                enemy_sprite.change_angle = (random.random() - 0.5) * 2
                enemy_sprite.size = 1

                self.asteroid_list.append(enemy_sprite)

        elif asteroid.size == 1:
            pass

    def on_update(self, x):
        """ Move everything """

        self.frame_count += 1

        if not self.game_over:
            self.asteroid_list.update()
            self.player_sprite_list.update()

            if not self.player_sprite.respawning:
                asteroids = arcade.check_for_collision_with_list(self.player_sprite, self.asteroid_list)
                if len(asteroids) > 0:
                    if self.lives > 0:
                        self.lives -= 1
                        self.player_sprite.respawn()
                        self.split_asteroid(cast(AsteroidSprite, asteroids[0]))
                        asteroids[0].remove_from_sprite_lists()
                        print("Crash")
                    else:
                        self.game_over = True
                        print("Game over")


def main():
    """ Start the game """
    window = MyGame()
    window.start_new_game()
    arcade.run()


if __name__ == "__main__":
    main()
