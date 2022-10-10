import arcade

# window properties
width = 400
height = 700
title = "Password Manager"


# loading page class
class LoadingView(arcade.View):
    def on_show(self):
        '''
        called to show the loading screen
        :return: none
        '''
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        '''
        draws items to screen
        :return: none
        '''
        arcade.start_render()
        # draws all text
        arcade.draw_text("PM", width / 2, 440, arcade.color.BRIGHT_NAVY_BLUE, 100, anchor_x="center", anchor_y="center",
                         font_name='Verdana Bold')
        arcade.draw_text("Password Manager", width / 2, 360, arcade.color.BRIGHT_NAVY_BLUE, 25, anchor_x="center",
                         anchor_y="center", font_name='Verdana Bold')
        arcade.draw_text("CD Tech", width / 2, 185, arcade.color.BLACK, 20, anchor_x="center", anchor_y="center",
                         font_name='Verdana Bold')
        arcade.draw_text("2021", width / 2, 150, arcade.color.BLACK, 20, anchor_x="center", anchor_y="center",
                         font_name='Verdana Bold')


# function to start loading screen
def main():
    window = arcade.Window(width, height, title)
    loading_view = LoadingView()
    window.show_view(loading_view)
    arcade.run()


main()
