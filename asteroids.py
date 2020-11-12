"""
Asteroid Smasher

Shoot space rocks in this demo program created with
Python and the Arcade library.

Artwork from http://kenney.nl
test 

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.asteroid_smasher
"""
import math
import os
import random
from typing import cast
import arcade

STARTING_ASTEROID_COUNT = 10
SCALE = 0.5
OFFSCREEN_SPACE = 300
SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 1000
SCREEN_TITLE = "Alman Achims awesome All-Adventure"
LEFT_LIMIT = -OFFSCREEN_SPACE
RIGHT_LIMIT = SCREEN_WIDTH + OFFSCREEN_SPACE
BOTTOM_LIMIT = -OFFSCREEN_SPACE
TOP_LIMIT = SCREEN_HEIGHT + OFFSCREEN_SPACE
NUMBER_OF_STARS = 101

class TurningSprite(arcade.Sprite):
    """ Sprite that sets its angle to the direction it is traveling in. """

    def update(self):
        """ Move the sprite """
        super().update()
        self.angle = math.degrees(math.atan2(self.change_y, self.change_x))

background_sound = arcade.load_sound("bayerischemusik.wav")
arcade.play_sound(background_sound)


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
        self.respawn_timer = 20



    def update(self):
        """
        Update our position and other particulars.
        """
        if self.respawning:
            self.respawning += 1
            self.alpha = self.respawning
            if self.respawning > 250:
                arcade.finish_render()
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


class Star:
    # star class for the background
    def __init__(self, position_x, position_y, radius, color):
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color
        self.start_position = position_x, position_y

    def draw(self):
        # Draw the star with the instance variables we have
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

    def reset_pos(self):
        # Reset the stars to a random spot above the screen
        self.position_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.position_x = random.randrange(SCREEN_WIDTH)

    def update(self):

        # Move the stars
        self.position_y -= 1
        self.position_x -= 0

        # See if the stars has fallen off the bottom of the screen.
        # If so, reset it.
        if self.position_y < 0:
            self.reset_pos()

        if self.position_x < 0:
            self.reset_pos()


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, fullscreen=True)
        arcade.set_background_color(arcade.csscolor.BLACK)

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
        self.ship_life_list = arcade.SpriteList()

        # Set up the player
        self.score = 0
        self.player_sprite = None
        self.lives = 0


        self.star_list = []

        color_list = [
            arcade.color.BLUE,
            arcade.color.WHITE,
            arcade.color.CELESTIAL_BLUE
        ]

        for i in range(NUMBER_OF_STARS):
            position_x = random.randrange(SCREEN_WIDTH)
            position_y = random.randrange(SCREEN_HEIGHT)
            radius = random.randrange(1, 2, 3)
            color = random.choice(color_list)

            star = Star(position_x, position_y, radius, color)

            self.star_list.append(star)

    def start_new_game(self):
        """ Set up the game and initialize the variables. """

        self.frame_count = 0
        self.game_over = False

        # Sprite lists
        self.player_sprite_list = arcade.SpriteList()
        self.asteroid_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.ship_life_list = arcade.SpriteList()

        # Set up the player
        self.score = 3
        self.player_sprite = ShipSprite("Adilette_1.png", SCALE)
        self.player_sprite_list.append(self.player_sprite)
        self.lives = 3

        # ToDo: Set up the little icons that represent the player lives.

        # Make the asteroids
        image_list = ("Potato2.png",
                      "Potato1.png",
                      "Potato3.png",
                      "Potato4.png")
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

        # Change the background.
        arcade.set_background_color(arcade.csscolor.BLACK)

        # This command has to happen before we start drawing
        arcade.start_render()

        for star in self.star_list:
            star.draw()

        # Draw all the sprites.
        self.asteroid_list.draw()
        self.bullet_list.draw()
        self.player_sprite_list.draw()
        self.ship_life_list.draw()

        # Put the text on the screen.
        output = f"Lifes left: {self.score}"
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
        self.score += 50

        if asteroid.size == 4:
            for i in range(3):
                image_no = random.randrange(2)
                image_list = ["Fries1.png",
                              "Fries2.png"]

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
                image_list = ["Fries1.png",
                              "Fries2.png"]

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
                image_list = ["Fries1.png",
                              "Fries2.png"]

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

        for star in self.star_list:
            star.update()

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

                        # Zeige "Crash!" Text an, sobald der Spieler mit einem Asteroiden kollidiert.
                        #Zeige "Crash!" so lange an, bis i=20 erreicht hat (Wusste nicht, wie man das mit Zeit macht)
                        i = 0.0
                        while i <= 20:
                            i += 0.1
                            start_x = SCREEN_WIDTH / 2
                            start_y = SCREEN_HEIGHT / 2
                            arcade.draw_text("Crash!", start_x, start_y,
                                             arcade.color.ANTIQUE_WHITE, 120, rotation=15)
                            arcade.finish_render()


                    else:
                        self.game_over = True





def main():
    """ Start the game """
    window = MyGame()
    window.start_new_game()
    arcade.run()


if __name__ == "__main__":
    main()
