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
        periodically called to draw items to screen
        :return: none
        '''
        arcade.start_render()
        # draw text
        arcade.draw_text("Recently Deleted", width / 2, 650, arcade.color.BRIGHT_NAVY_BLUE, 18,
                         anchor_x="center", font_name='Verdana Bold')
        arcade.draw_text("< Back", 15, 652, arcade.color.BLACK, 14, font_name='Verdana Bold')
        arcade.draw_text("Select", 322, 652, arcade.color.BLACK, 14, font_name='Verdana Bold')
        arcade.draw_text("Delete All", 285, 30, arcade.color.BLACK, 14, font_name='Verdana Bold')
        arcade.draw_text("Recover All", 15, 30, arcade.color.BLACK, 14, font_name='Verdana Bold')
        # draw colors
        arcade.draw_rectangle_filled(width / 2, 560, 350, 100, arcade.color.DARK_GRAY)
        # draw text
        arcade.draw_text("Passwords will be permanently", width / 2, 565, arcade.color.WHITE, 16,
                         anchor_x="center", font_name='Verdana')
        arcade.draw_text("deleted after 30 days", width / 2, 535, arcade.color.WHITE, 16,
                         anchor_x="center", font_name='Verdana')
        arcade.draw_text("30 Days Left", 35, 465, arcade.color.BLACK, 22, font_name='Verdana Bold')
        arcade.draw_rectangle_filled(width / 2, 420, 350, 70, arcade.color.BLACK)
        arcade.draw_text("LinkedIn", 50, 415, arcade.color.WHITE, 22)
        arcade.draw_text("Username: CD Tech", 50, 395, arcade.color.WHITE, 12)
        # draw icons
        self.icon_list: arcade.SpriteList = arcade.SpriteList()
        remove = Icon("Images/3.png", 0.04)
        remove.position = 340, 420
        self.icon_list.append(remove)
        recover = Icon("Images/4.png", 0.04)
        recover.position = 270, 420
        self.icon_list.append(recover)
        self.icon_list.draw()
        # draw text
        arcade.draw_text("19 Days Left", 35, 340, arcade.color.BLACK, 22, font_name='Verdana Bold')

        arcade.draw_rectangle_filled(width / 2, 295, 350, 70, arcade.color.BLACK)
        arcade.draw_text("Instagram", 50, 290, arcade.color.WHITE, 22)
        arcade.draw_text("Username: cd_technologies", 50, 270, arcade.color.WHITE, 12)
        # draw icon
        self.icon_list: arcade.SpriteList = arcade.SpriteList()
        remove = Icon("Images/3.png", 0.04)
        remove.position = 340, 295
        self.icon_list.append(remove)
        recover = Icon("Images/4.png", 0.04)
        recover.position = 270, 295
        self.icon_list.append(recover)
        self.icon_list.draw()
        # draw text
        arcade.draw_rectangle_filled(width / 2, 215, 350, 70, arcade.color.BLACK)
        arcade.draw_text("Facebook", 50, 210, arcade.color.WHITE, 22)
        arcade.draw_text("Username: cd_tech_", 50, 190, arcade.color.WHITE, 12)
        # draw recover can icon
        self.icon_list: arcade.SpriteList = arcade.SpriteList()
        remove = Icon("Images/3.png", 0.04)
        remove.position = 340, 215
        self.icon_list.append(remove)
        # draw delete icon
        recover = Icon("Images/4.png", 0.04)
        recover.position = 270, 215
        self.icon_list.append(recover)
        self.icon_list.draw()


# generic icon class
class Icon(arcade.Sprite):
    def __init__(self, filename, scale):
        '''
        creates icon
        :param filename: locaiton of icon image
        :param scale: icon image scale
        '''
        super().__init__(filename=filename, scale=scale)


# call to open this window
def main():
    window = arcade.Window(width, height, title)
    main_view = MainView()
    window.show_view(main_view)
    arcade.run()


main()
