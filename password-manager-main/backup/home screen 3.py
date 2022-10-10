import arcade
import arcade.gui
from arcade.gui import UIManager

width = 400
height = 700
title = "Password Manager"

passwordlistname = ["Instagram", "Amazon", "Presto", "Instagram", "Jstor", "Tim Hortons"]
passwordlistusername = ["cd_technologies", "cdtech@gmail.com", "cd_travels", "@cd_tech", "cdtech@gmail.com", "cdtech@gmail.com"]

class MainView(arcade.View):
    def __init__(self):
        super().__init__()
        self.sprite_list = arcade.SpriteList()
        self.ui_manager = UIManager()

    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)
        self.on_draw()

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()

    def on_draw(self):
        arcade.start_render()
        y = 635
        arcade.draw_text("PASSWORDS", width / 2, y, arcade.color.BRIGHT_NAVY_BLUE, 28,
                         anchor_x="center", font_name='Verdana Bold')

        self.pile_mat_list: arcade.SpriteList = arcade.SpriteList()

        settings = Icon("../Images/2.png", 0.04)
        settings.position = 35, 657
        self.pile_mat_list.append(settings)

        add = Icon("../Images/1.png", 0.04)
        add.position = 365, 658
        self.pile_mat_list.append(add)

        self.pile_mat_list.draw()

        if len(passwordlistname) == 0:
            arcade.draw_rectangle_filled(width / 2, 500, 340, 200, arcade.color.BLACK)
            arcade.draw_text("Click the '+' to add", width / 2, 510, arcade.color.WHITE, 24,
                             anchor_x="center", font_name='Verdana')
            arcade.draw_text("your first password", width / 2, 465, arcade.color.WHITE, 24,
                             anchor_x="center", font_name='Verdana')
        else:
            self.remove_list: arcade.SpriteList = arcade.SpriteList()
            for x in range(len(passwordlistname)):
                arcade.draw_rectangle_filled(width / 2, 575 - (80*x), 350, 70, arcade.color.BLACK)
                remove = Icon("../Images/3.png", 0.04)
                remove.position = 340, 575 - (80*x)
                self.remove_list.append(remove)
                button = MyFlatButton(passwordlistname[x], center_x=165, center_y=585-(80*x), width=280, height=35)
                self.ui_manager.add_ui_element(button)
            self.remove_list.draw()

            for x in range(len(passwordlistname)):
                arcade.draw_text("Username: " + passwordlistusername[x], 165, 545 - (80 * x), arcade.color.WHITE, 12,
                                 font_name='Verdana', anchor_x="center")
            arcade.draw_rectangle_filled(width/2, 575 - (80*(len(passwordlistname))), 350, 70, arcade.color.BLACK)
            arcade.draw_text("Recently Deleted", width / 2, 560 - (80*(len(passwordlistname))), arcade.color.RADICAL_RED, 20, anchor_x="center")


class Icon(arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename=filename, scale=scale)


class MyFlatButton(arcade.gui.UIFlatButton):
    def on_click(self):
        print("Clicked")


def main():
    window = arcade.Window(width, height, title)
    main_view = MainView()
    window.show_view(main_view)
    arcade.run()


main()
