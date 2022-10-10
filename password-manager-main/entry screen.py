# import library
import arcade
import globalValues
import arcade.gui
from arcade.gui import UIManager

# window details
width = 400
height = 700
title = "Password Manager"


# create new entry button class
class Button(arcade.gui.UIFlatButton):
    def __init__(self, center_x, center_y, str, ui_manager):
        '''
        creates the button class
        :param center_x: center of the button, x axis
        :param center_y: center of the button, y axis
        :param str: text on the button
        :param ui_manager: button manager
        '''
        super().__init__(center_x=center_x, center_y=center_y, text=str)
        self.ui_manager = ui_manager

    def on_click(self):
        '''
        called when the button is pressed
        :return:
        '''
        self.ui_manager.purge_ui_elements()


# creates a button that generates a new password
class GeneratePasswordButton(arcade.gui.UIFlatButton):
    def __init__(self, str, center_x, center_y, ui_manager):
        '''
        generates a new button
        :param str: text of button
        :param center_x: center of button in x direction
        :param center_y: center of button in y direction
        :param ui_manager: manages button
        '''
        super().__init__(str, center_x=center_x, center_y=center_y)
        self.ui_manager = ui_manager

    def on_click(self):
        '''
        called when the button is clicked
        :return:
        '''
        input_box = arcade.gui.UIInputBox(center_x=260, center_y=320, width=260)
        input_box.text = 's3nHyU%ank#Kl'
        input_box.cursor_index = len(input_box.text)
        self.ui_manager.add_ui_element(input_box)


# main new entry screen class/view
class EntryScreen(arcade.View):

    def __init__(self):
        '''
        creates new entry screen view
        '''
        super().__init__()
        arcade.set_background_color(arcade.color.BLACK)
        self.ui_manager = UIManager()

    def on_draw(self):
        '''
        draws the text to the screen
        :return: none
        '''
        arcade.start_render()
        arcade.draw_text("Nickname:", start_x=20, start_y=600, color=arcade.color.WHITE, font_size=20)
        arcade.draw_text("URL:", start_x=20, start_y=500, color=arcade.color.WHITE, font_size=20)
        arcade.draw_text("Username:", start_x=20, start_y=400, color=arcade.color.WHITE, font_size=20)
        arcade.draw_text("Password:", start_x=20, start_y=300, color=arcade.color.WHITE, font_size=20)
        arcade.draw_text("Entry added!", start_x=125, start_y=180, color=arcade.color.WHITE, font_size=20)

    def on_show_view(self):
        '''
        first method called, calls the setup function
        :return:
        '''
        self.setup()

    def on_hide_view(self):
        '''
        hides this view
        :return: none
        '''
        self.ui_manager.unregister_handlers()

    def setup(self):
        '''
        sets up the view, called only once
        :return: none
        '''
        # creates an object of a global value class shared accross the project
        global_values = globalValues.GlobalValues()
        self.ui_manager.purge_ui_elements()
        # add button
        button = Button(str="Create entry", center_x=200, center_y=200, ui_manager=self.ui_manager)
        self.ui_manager.add_ui_element(button)
        # input box nickname
        input_box = arcade.gui.UIInputBox(center_x=260, center_y=620, width=255)
        input_box.text = ''
        input_box.cursor_index = len(input_box.text)
        self.ui_manager.add_ui_element(input_box)
        # input box url
        input_box = arcade.gui.UIInputBox(center_x=230, center_y=520, width=320)
        input_box.text = ''
        input_box.cursor_index = len(input_box.text)
        self.ui_manager.add_ui_element(input_box)
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
        # generate password
        generate_password = GeneratePasswordButton(str="Generate password", center_x=260, center_y=280,
                                                   ui_manager=self.ui_manager)
        self.ui_manager.add_ui_element(generate_password)


def main():
    '''
    main function to call this view
    :return: none
    '''
    window = arcade.Window(title="Test", width=400, height=700)
    page = EntryScreen()
    window.show_view(page)
    arcade.run()


main()
