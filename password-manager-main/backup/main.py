import arcade
import globalValues
#window properties
width = 400
height = 700
title = "passwordapp"

#main
class Main(arcade.Window):

    def __init__(self):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)
        global_values = globalValues.GlobalValues()
        print(global_values.password)

    def setup(self):
        arcade.start_render()
        arcade.draw_rectangle_filled(200, 0, 400, 150, arcade.color.LIGHT_GRAY)


def main():
    window = Main()
    window.setup()
    arcade.run()


main()
