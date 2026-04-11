import arcade



class WinScreen_(arcade.View):
    def __init__(self):
        super().__init__()

    def on_draw(self):
        arcade.draw_text("YOU WIN!!", 850, 1000, arcade.color.WHITE, 50)
        #arcade.draw_text("INVIO: Torna al menu principale", 850, 900, arcade.color.WHITE, 20)
        arcade.draw_text("Premi ESC per chiudere il gioco", 850, 900, arcade.color.WHITE, 20)
        #arcade.draw_text("Hai guadagnato" + str(MyGame.conta_monete_prese) + " monete e " + str(MyGame.conta_diamanti_presi) + " diamanti", 850, 850, arcade.color.WHITE, 20)
        arcade.draw_text("Premi R per rigiocare", 850, 850, arcade.color.WHITE, 20) 
   