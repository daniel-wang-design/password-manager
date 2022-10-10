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
        arcade.draw_text("Recently Deleted", width / 2, 650, arcade.color.BRIGHT_NAVY_BLUE, 18,
                         anchor_x="center", font_name='Verdana Bold')
        arcade.draw_text("< Back", 15, 652, arcade.color.BLACK, 14, font_name='Verdana Bold')
        arcade.draw_text("Select", 322, 652, arcade.color.BLACK, 14, font_name='Verdana Bold')
        arcade.draw_text("Delete All", 285, 30, arcade.color.BLACK, 14, font_name='Verdana Bold')
        arcade.draw_text("Recover All", 15, 30, arcade.color.BLACK, 14, font_name='Verdana Bold')

        arcade.draw_rectangle_filled(width / 2, 560, 350, 100, arcade.color.DARK_GRAY)
        arcade.draw_text("Passwords will be permanently", width / 2, 565, arcade.color.WHITE, 16,
                         anchor_x="center", font_name='Verdana')
        arcade.draw_text("deleted after 30 days", width / 2, 535, arcade.color.WHITE, 16,
                         anchor_x="center", font_name='Verdana')

        arcade.draw_text("30 Days Left", 35, 465, arcade.color.BLACK, 22, font_name='Verdana Bold')

        arcade.draw_rectangle_filled(width / 2, 420, 350, 70, arcade.color.BLACK)
        arcade.draw_text("LinkedIn", 50, 415, arcade.color.WHITE, 22)
        arcade.draw_text("Username: CD Tech", 50, 395, arcade.color.WHITE, 12)

        self.icon_list: arcade.SpriteList = arcade.SpriteList()
        remove = Icon("Images/3.png", 0.04)
        remove.position = 340, 420
        self.icon_list.append(remove)
        recover = Icon("Images/4.png", 0.04)
        recover.position = 270, 420
        self.icon_list.append(recover)
        self.icon_list.draw()

        arcade.draw_text("19 Days Left", 35, 340, arcade.color.BLACK, 22, font_name='Verdana Bold')

        arcade.draw_rectangle_filled(width / 2, 295, 350, 70, arcade.color.BLACK)
        arcade.draw_text("Facebook", 50, 290, arcade.color.WHITE, 22)
        arcade.draw_text("Username: cd_tech_", 50, 270, arcade.color.WHITE, 12)

        self.icon_list: arcade.SpriteList = arcade.SpriteList()
        remove = Icon("Images/3.png", 0.04)
        remove.position = 340, 295
        self.icon_list.append(remove)
        recover = Icon("Images/4.png", 0.04)
        recover.position = 270, 295
        self.icon_list.append(recover)
        self.icon_list.draw()


class Icon(arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename=filename, scale=scale)

def main():
    window = arcade.Window(width, height, title)
    main_view = MainView()
    window.show_view(main_view)
    arcade.run()


main()
