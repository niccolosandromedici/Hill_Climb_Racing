# import arcade
# from Gioco_ import MyGame

# class MenuView(arcade.View):
#     def __init__(self):
#         super().__init__()
#         self.sto_giocando = False
#         self.gioco_view = MyGame(900, 600, "Gioco")

#     def on_draw(self):
#         if self.sto_giocando == True:
#             self.clear()    
#             self.gioco_view.on_draw()
#         arcade.draw_text("MENU PRINCIPALE", 1000, 1000,
#                          arcade.color.WHITE, font_size=48, anchor_x="center")
#         arcade.draw_text("INVIO: Inizia nuova partita    ESC: Esci",
#                          1000, 800, arcade.color.LIGHT_GRAY, font_size=16, anchor_x="center")
        
#     def on_update(self, delta_time):
#         #movimento camera
#         if self.sto_giocando == False:
#             self.camera.position = self.macchina1.position
#         else:
#             self.camera.position = (1000, 1000)

#     def on_key_press(self, key, modifiers):

#         if key == arcade.key.ENTER:
#             # Iniziamo una nuova partita
#             self.sto_giocando = True
#             self.window.show_view(self.gioco_view)

#         elif key == arcade.key.ESCAPE:
#             # Chiudiamo la finestra per uscire dal gioco
#             self.window.close()