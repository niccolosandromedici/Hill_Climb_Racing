import arcade


class GameOver_(arcade.View):
    def __init__(self):
        super().__init__()

    def on_draw(self):
        arcade.draw_text("GAME OVER", 850, 1000, arcade.color.WHITE, 50)
    
   

    

    