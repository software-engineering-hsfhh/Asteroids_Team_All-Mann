"""
This program shows how to:
  * Display a sequence of screens in your game.  The "arcade.View"
    class makes it easy to separate the code for each screen into
    its own class.
  * This example shows the absolute basics of using "arcade.View".
    See the "different_screens_example.py" for how to handle
    screen-specific data.

Make a separate class for each view (screen) in your game.
The class will inherit from arcade.View. The structure will
look like an arcade.Window as each View will need to have its own draw,
update and window event methods. To switch a View, simply create a View
with `view = MyView()` and then use the "self.window.set_view(view)" method.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.view_screens_minimal
"""

import arcade


WIDTH = 1600
HEIGHT = 900


class GameView(arcade.View):
    """ Manage the 'game' view for our program. """

    def __init__(self):
        super().__init__()
        # Create variables here

    def setup(self):
        """ This should set up your game and get it ready to play """
        # Replace 'pass' with the code to set up your game
        pass

    def on_show(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """ Draw everything for the game. """
        arcade.start_render()
        arcade.draw_text("Achim Allmann ist auf einer ewig währenden Reise durchs Weltall auf\n"
                         "der Suche nach dem Sinn des Lebens als plötzlich eine bösartige\n"
                         "Gruppe Asteroiden auftaucht!\n\n\nDrücke die Leertaste, um fortzufahren", WIDTH/2, HEIGHT/2,
                         arcade.color.WHITE, font_size=25, anchor_x="center")

    def on_key_press(self, key, _modifiers):
        """Drücke Leertaste um fortzufahren"""
        if key == arcade.key.SPACE:
            self.game_over = True
            print ("Game Over")




def main():
    """ Startup """
    window = arcade.Window(1600, 900, "Asteroids",  fullscreen=False)
    Game_View = GameView()
    window.show_view(Game_View)
    arcade.run()


if __name__ == "__main__":
    main()