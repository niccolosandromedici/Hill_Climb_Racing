import arcade
from Gioco_ import MyGame

class MenuView(arcade.View):
    def __init__(self):
        super().__init__()

    def on_draw(self):
        self.clear()
        arcade.draw_rect_filled(
            arcade.XYWH(480, 270, 900, 600),
            (1,1,1,1)  # nero
        )
        arcade.draw_text("Hill Climb Racing",
                         # MyGame().camera.position[0] - MyGame().SCREEN_WIDTH//50, MyGame().camera.position[1],
                         480, 350,
                         arcade.color.WHITE, font_size=48, anchor_x="center")
        arcade.draw_text("INVIO: Inizia nuova partita    ESC: Chiudi il gioco",
                         480, 250,
                         # MyGame().camera.position[0] - MyGame().SCREEN_WIDTH//50, MyGame().camera.position[1]-100,
                         arcade.color.LIGHT_GRAY, font_size=16, anchor_x="center")
        
    

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ENTER:
            gioco_view = MyGame()
            # Iniziamo una nuova partita
            self.window.show_view(gioco_view)

        elif key == arcade.key.ESCAPE:
            # Chiudiamo la finestra per uscire dal gioco
            self.window.close()
