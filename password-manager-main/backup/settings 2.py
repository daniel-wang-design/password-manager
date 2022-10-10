import arcade
import arcade.gui

width = 400
height = 700
title = "Password Manager"


class MainView(arcade.View):
    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Settings", width / 2, 650, arcade.color.BRIGHT_NAVY_BLUE, 20,
                         anchor_x="center", font_name='Verdana Bold')
        arcade.draw_rectangle_filled(width / 2, 615, 350, 40, arcade.color.DARK_GRAY)
        arcade.draw_text("Search", 30, 603, arcade.color.LIGHT_GRAY, 16, font_name='Verdana Bold')
        arcade.draw_text("< Back", 15, 652, arcade.color.BLACK, 16, font_name='Verdana Bold')

        arcade.draw_text("Profile", 30, 550, arcade.color.BLACK, 16, font_name='Verdana Bold')
        arcade.draw_text(">", 340, 550, arcade.color.BLACK, 16, font_name='Verdana Bold')

        arcade.draw_text("Manage Tags", 30, 500, arcade.color.BLACK, 16, font_name='Verdana Bold')
        arcade.draw_text(">", 340, 500, arcade.color.BLACK, 16, font_name='Verdana Bold')

        arcade.draw_text("Require Login to View", 30, 450, arcade.color.BLACK, 16, font_name='Verdana Bold')
        arcade.draw_text("Passwords", 30, 425, arcade.color.BLACK, 16, font_name='Verdana Bold')

        self.on_off_list: arcade.SpriteList = arcade.SpriteList()
        on = Icon("Images/5.png", 0.07)
        on.position = 340, 460
        self.on_off_list.append(on)
        self.on_off_list.draw()

        arcade.draw_text("Theme", 30, 375, arcade.color.BLACK, 16, font_name='Verdana Bold')
        arcade.draw_text(">", 340, 375, arcade.color.BLACK, 16, font_name='Verdana Bold')

        arcade.draw_text("Advanced Settings", 30, 325, arcade.color.BLACK, 16, font_name='Verdana Bold')
        arcade.draw_text(">", 340, 325, arcade.color.BLACK, 16, font_name='Verdana Bold')

        arcade.draw_text("Privacy Policy", 30, 275, arcade.color.BLACK, 16, font_name='Verdana Bold')
        arcade.draw_text(">", 340, 275, arcade.color.BLACK, 16, font_name='Verdana Bold')

        arcade.draw_text("About", 30, 225, arcade.color.BLACK, 16, font_name='Verdana Bold')
        arcade.draw_text(">", 340, 225, arcade.color.BLACK, 16, font_name='Verdana Bold')

        arcade.draw_text("Help", 30, 175, arcade.color.BLACK, 16, font_name='Verdana Bold')
        arcade.draw_text(">", 340, 175, arcade.color.BLACK, 16, font_name='Verdana Bold')

        arcade.draw_text("Add Account", 30, 125, arcade.color.BRIGHT_NAVY_BLUE, 16, font_name='Verdana')
        arcade.draw_text("Logout", 30, 75, arcade.color.BRIGHT_NAVY_BLUE, 16, font_name='Verdana')

class Icon(arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename=filename, scale=scale)

def main():
    window = arcade.Window(width, height, title)
    main_view = MainView()
    window.show_view(main_view)
    arcade.run()


main()
