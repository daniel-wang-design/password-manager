import arcade
import globalValues
import arcade.gui
from arcade.gui import UIManager

# window properties
width = 400
height = 700
title = "Password Manager"


# generic button class
class Button(arcade.gui.UIFlatButton):
    def __init__(self, center_x, center_y, str, ui_manager, width):
        '''
        creates a button
        :param center_x: center of the button in x direction
        :param center_y: center of the button in y direction
        :param str: text on button
        :param ui_manager: manages button
        :param width: width of button
        '''
        super().__init__(center_x=center_x, center_y=center_y, text=str, width=width)
        self.ui_manager = ui_manager

    def on_click(self):
        '''
        called when button is clicked
        :return: none
        '''
        self.ui_manager.purge_ui_elements()


# main login screen
class EntryScreen(arcade.View):

    def __init__(self):
        '''
        initiates screen
        '''
        super().__init__()
        arcade.set_background_color(arcade.color.BLACK)
        self.ui_manager = UIManager()

    def on_draw(self):
        '''
        called periodically to draw items to screen
        :return:
        '''
        arcade.start_render()
        # draw text
        arcade.draw_text("Log in to your account", start_x=20, start_y=600, color=arcade.color.WHITE, font_size=30)
        arcade.draw_text(".......................................................", start_x=20, start_y=500,
                         color=arcade.color.WHITE, font_size=20)
        arcade.draw_text("Username:", start_x=20, start_y=400, color=arcade.color.WHITE, font_size=20)
        arcade.draw_text("Password:", start_x=20, start_y=300, color=arcade.color.WHITE, font_size=20)
        arcade.draw_text("Logged in!", start_x=125, start_y=180, color=arcade.color.WHITE, font_size=20)

    def on_show_view(self):
        '''
        called to show this screen
        :return:
        '''
        self.setup()

    def on_hide_view(self):
        '''
        called to hide this view
        :return:
        '''
        self.ui_manager.unregister_handlers()

    def setup(self):
        '''
        called once when created
        :return: none
        '''
        # setting up common values for all files
        global_values = globalValues.GlobalValues()
        self.ui_manager.purge_ui_elements()
        # add button
        button = Button(str="Log in", center_x=200, center_y=200, ui_manager=self.ui_manager, width=200)
        self.ui_manager.add_ui_element(button)
        # input box username
        input_box = arcade.gui.UIInputBox(center_x=265, center_y=420, width=250)
        input_box.text = ''
        input_box.cursor_index = len(input_box.text)
        self.ui_manager.add_ui_element(input_box)
        # input box password
        input_box = arcade.gui.UIInputBox(center_x=260, center_y=320, width=260)
        input_box.text = ''
        input_box.cursor_index = len(input_box.text)
        self.ui_manager.add_ui_element(input_box)


# function to load window
def main():
    window = arcade.Window(title="Test", width=400, height=700)
    page = EntryScreen()
    window.show_view(page)
    arcade.run()


main()
