import arcade
import arcade.gui

# window properties
width = 400
height = 700
title = "Password Manager"


# main window
class MainView(arcade.View):
    def __init__(self):
        '''
        initiates window
        '''
        super().__init__()
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        '''
        called periodically to draw screen
        :return: none
        '''
        arcade.start_render()
        # draw tags text
        arcade.draw_text("Tags", width / 2, 650, arcade.color.BRIGHT_NAVY_BLUE, 20,
                         anchor_x="center", font_name='Verdana Bold')
        self.pile_mat_list: arcade.SpriteList = arcade.SpriteList()
        # draw icon
        add = Icon("Images/1.png", 0.03)
        add.position = 365, 664
        self.pile_mat_list.append(add)
        self.pile_mat_list.draw()
        arcade.draw_rectangle_filled(width / 2, 615, 350, 40, arcade.color.DARK_GRAY)
        # draw search bar
        arcade.draw_text("Search", 30, 603, arcade.color.LIGHT_GRAY, 16, font_name='Verdana Bold')
        # back bar
        arcade.draw_text("< Back", 15, 652, arcade.color.BLACK, 16, font_name='Verdana Bold')
        # draw tags
        arcade.draw_text("Social Media (2)", 30, 550, arcade.color.PURPLE, 16, font_name='Verdana Bold')
        arcade.draw_text("edit", 300, 546, arcade.color.BRIGHT_NAVY_BLUE, 14, font_name='Verdana Bold')
        arcade.draw_text("View Passwords", 30, 525, arcade.color.BLACK, 12, font_name='Verdana Bold')
        # tags
        arcade.draw_text("School (1)", 30, 475, arcade.color.RED, 16, font_name='Verdana Bold')
        arcade.draw_text("edit", 300, 471, arcade.color.BRIGHT_NAVY_BLUE, 14, font_name='Verdana Bold')
        arcade.draw_text("View Passwords", 30, 450, arcade.color.BLACK, 12, font_name='Verdana Bold')
        # tags
        arcade.draw_text("Travel (1)", 30, 400, arcade.color.FOREST_GREEN, 16, font_name='Verdana Bold')
        arcade.draw_text("edit", 300, 396, arcade.color.BRIGHT_NAVY_BLUE, 14, font_name='Verdana Bold')
        arcade.draw_text("View Passwords", 30, 375, arcade.color.BLACK, 12, font_name='Verdana Bold')
        # tags
        arcade.draw_text("Food (1)", 30, 325, arcade.color.ORANGE, 16, font_name='Verdana Bold')
        arcade.draw_text("edit", 300, 321, arcade.color.BRIGHT_NAVY_BLUE, 14, font_name='Verdana Bold')
        arcade.draw_text("View Passwords", 30, 300, arcade.color.BLACK, 12, font_name='Verdana Bold')


# generic icon class
class Icon(arcade.Sprite):

    def __init__(self, filename, scale):
        '''
        initiates icon
        :param filename: file location of image
        :param scale: scale of icon image
        '''
        super().__init__(filename=filename, scale=scale)


# called to show this window
def main():
    window = arcade.Window(width, height, title)
    main_view = MainView()
    window.show_view(main_view)
    arcade.run()


main()
