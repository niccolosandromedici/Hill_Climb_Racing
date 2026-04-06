import arcade
from Gioco_ import MyGame

class MenuView(arcade.View):
    def __init__(self):
        super().__init__()

    def on_draw(self):
        arcade.draw_text("MENU PRINCIPALE", 480, 350,
                         arcade.color.WHITE, font_size=48, anchor_x="center")
        arcade.draw_text("INVIO: Inizia nuova partita    ESC: Esci",
                         480, 250, arcade.color.LIGHT_GRAY, font_size=16, anchor_x="center")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ENTER:
            # Iniziamo una nuova partita
            self.window.show_view(MyGame(900, 600, "Gioco"))
        elif key == arcade.key.ESCAPE:
            # Chiudiamo la finestra per uscire dal gioco
            self.window.close()