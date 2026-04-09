import arcade
from Gioco_ import MyGame

class MenuView(arcade.View):
    def __init__(self):
        super().__init__()

    def on_draw(self):
        self.clear()
        arcade.draw_rect_filled(
            arcade.XYWH(-200, -200, 10000, 10000),
            (1,1,1,1)  # bianco
        )
        arcade.draw_text("MENU PRINCIPALE", MyGame().camera.position[0]-MyGame.SCREEN_WIDTH//50, MyGame().camera.position[1],
                         arcade.color.WHITE, font_size=48, anchor_x="center")
        arcade.draw_text("INVIO: Inizia nuova partita    ESC: Esci",
                         MyGame().camera.position[0]-MyGame.SCREEN_WIDTH//50, MyGame().camera.position[1]-100, arcade.color.LIGHT_GRAY, font_size=16, anchor_x="center")
        
    

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ENTER:
            gioco_view = MyGame()
            gioco_view.setup()
            # Iniziamo una nuova partita
            self.window.show_view(gioco_view)

        elif key == arcade.key.ESCAPE:
            # Chiudiamo la finestra per uscire dal gioco
            self.window.close()