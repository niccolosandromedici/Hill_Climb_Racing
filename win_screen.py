import arcade


class WinScreen_:
    def __init__(self):
        super().__init__()

    def on_draw(self):
        arcade.draw_text("YOU WIN!!", 850, 1000, arcade.color.WHITE, 50)
    
   