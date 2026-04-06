import arcade
import os
import random
import Muri
import Player





#https://api.arcade.academy/en/stable/tutorials/platform_tutorial/step_07.html
#sito con tutta la documentazione necessaria per il mio gioco

#https://api.arcade.academy/en/3.3.3/example_code/background_parallax.html
#sito per errore di parallasse

SCREEN_WIDTH : int = 900
SCREEN_HEIGHT : int = 600
COLLEZIONABILI_WIDTH : int = 32
COLLEZIONABILI_HEIGHT : int = 32
    
class MyGame(arcade.Window):
   

    def __init__(self, width, height, title):

        super().__init__(width, height, title)
        #self.parallasse = parallasse.parallax()
        #self.macchina_list = arcade.SpriteList()
        self.moneta_list = arcade.SpriteList()
        
        #suono
        self.suono_motore = arcade.load_sound("./immagini/audio_motore.mp3")
        
        # #fisica
        #self.gravity : int | float = 1
        # #self.jump_speed : int | float = 20

        # #movimento
        #self.velocita : int | float | bool = None
        #self.velocita_angle : int| float = 1
        
        #conta monete e diamanti
        self.conta_monete_prese : int = 0
        self.conta_diamanti_presi : int = 0

        self.testo_score_monete : str | bool = None
        self.testo_score_diamanti : str | bool = None

        self.setup()
        #self.parallasse.pan_camera_to_player()
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        Player.Macchina1().up_pressed : bool = False
        Player.Macchina1().down_pressed : bool = False
        Player.Macchina1().left_pressed : bool = False
        Player.Macchina1().right_pressed : bool = False

        Player.Macchina1().__init__()
        
        

        # Create a Platformer Physics Engine.
        # This will handle moving our player as well as collisions between
        # the player sprite and whatever SpriteList we specify for the walls.
        # It is important to supply static platforms to the walls parameter. There is a
        # platforms parameter that is intended for moving platforms.
        # If a platform is supposed to move, and is added to the walls list,
        # it will not be moved.
        #self.physics_engine = arcade.PhysicsEnginePlatformer(Player.Macchina1().macchina1, walls = Muri.Muri_().wall_list, gravity_constant = self.gravity)
        
        
        

    def setup(self):



        #crea macchina
        Player.Macchina1().setup()


        #crea monete iniziali
        for i in range(5):
            self.crea_monete(tipo = "oro")
        self.crea_monete(tipo = "diamante")

        # Set up the camera
        self.camera = arcade.Camera2D()
        

        #carica sfondo
        self.background = arcade.load_texture("./immagini/Sfondo_STRADA.png")
        
        #scrivi testo punteggio delle monete
        self.testo_score_monete = arcade.Text( #testo del punteggio
            text="Monete: " + str(self.conta_monete_prese),
            x = Player.Macchina1().center_x,
            y = Player.Macchina1().center_y + 250,
            color = arcade.color.BLACK,
            font_size = 24,
            font_name = "Arial", # O il nome del tuo font caricato
            anchor_x = "center" # Allinea il testo a sinistra
        )

        #scrivi testo punteggio dei diamanti
        self.testo_score_diamanti = arcade.Text( #testo del punteggio
            text="Diamanti: " + str(self.conta_diamanti_presi),
            x = Player.Macchina1().center_x,
            y = Player.Macchina1().center_y + 300, 
            color = arcade.color.BLACK,
            font_size = 24,
            font_name = "Arial", # O il nome del tuo font caricato
            anchor_x = "center" # Allinea il testo a sinistra
        )


   
        


    
    def crea_monete(self, tipo):

        #print("[" + str(self.conta_monete_prese) + "] == > Creazione monete...")


        next_x = Player.Macchina1().center_x

        while abs(next_x - Player.Macchina1().center_x) < 100 :
            next_x = ((COLLEZIONABILI_HEIGHT/2) + (Player.Macchina1().center_x + random.randint(100, (SCREEN_WIDTH - COLLEZIONABILI_WIDTH)))%(SCREEN_WIDTH - COLLEZIONABILI_WIDTH)) + Player.Macchina1().center_x + 1000

        next_y: int = 330          
        
        #print("[",self.macchina1.center_x,"][", self.macchina1.center_y,"] = > moneta creata in: [",next_x, "] [", next_y, "]")


        

        if tipo == "oro":
            self.moneta = arcade.Sprite("./immagini/Moneta_senza_sfondo.png")
            self.moneta.center_x = next_x
            self.moneta.center_y = next_y
            self.moneta.scale = 0.2
            self.moneta.tipo = "oro"
            self.moneta_list.append(self.moneta)

        if tipo == "diamante":
            self.moneta = arcade.Sprite("./immagini/Diamante.png")
            self.moneta.center_x = next_x
            self.moneta.center_y = next_y
            self.moneta.scale = 0.2
            self.moneta.tipo = "diamante"
            self.moneta_list.append(self.moneta)

        
    def rimuovi_moneta(self, Sprite_moneta):
        Sprite_moneta.remove_from_sprite_lists()
        #print("Moneta scomparsa!")
    def rimuovi_diamante(self, Sprite_moneta):
        Sprite_moneta.remove_from_sprite_lists()
        #print("Diamante scomparso!")




    def on_draw(self):
        self.clear()
        self.camera.use()
        #self.parallasse.camera.use()
        arcade.draw_texture_rect(self.background, arcade.types.Viewport( self.camera.position[0] - SCREEN_WIDTH/2, self.camera.position[1] - SCREEN_HEIGHT/3.2, SCREEN_WIDTH + 100, SCREEN_HEIGHT + 100) )
        
        #bg = self.parallasse.backgrounds

        # Sposta i layer simulando la profondità
        #bg.offset = self.camera.bottom_left
        # Segue la camera per simulare un "mondo infinito"
        #bg.pos = self.camera.bottom_left

        #bg.draw()
        #arcade.draw_sprite(self.macchina1)
        self.moneta_list.draw()

        Player.Macchina1().on_draw()
        
        Muri.Muri_().draw()
        self.testo_score_monete.draw()
        self.testo_score_diamanti.draw()



    def on_update(self, delta_time):

        self.camera.position = Player.Macchina1().macchina1.position
        #self.parallasse.on_update(delta_time)
        #self.physics_engine.update()

        Player.Macchina1().on_update(delta_time)

        #aggiornamento x delle scritte
        self.testo_score_monete.x += Player.Macchina1().change_x
        self.testo_score_diamanti.x += Player.Macchina1().change_x

        # Gestione collisioni tra macchina e collezionabili
        collisioni_macchina_collezzionabili = arcade.check_for_collision_with_list(Player.Macchina1().macchina1, self.moneta_list)        
        if len(collisioni_macchina_collezzionabili) > 0: # Vuol dire che il personaggio si è scontrato con qualcosa
            if collisioni_macchina_collezzionabili[0].tipo == "oro":
                self.conta_monete_prese += 1
                self.testo_score_monete.text = f"Monete: {self.conta_monete_prese}"
                collisioni_macchina_collezzionabili[0].remove_from_sprite_lists()
                self.crea_monete(tipo = "oro")
                #print("moneta presa! Punteggio:", self.conta_monete_prese)
            elif collisioni_macchina_collezzionabili[0].tipo == "diamante":
                self.conta_diamanti_presi += 1
                self.testo_score_diamanti.text = f"Diamanti: {self.conta_diamanti_presi}"
                collisioni_macchina_collezzionabili[0].remove_from_sprite_lists()
                self.crea_monete(tipo = "diamante")
                #print("Diamante preso! Punteggio:", self.conta_diamanti_presi)

    
        
        # Calcola movimento in base ai tasti premuti
        Player.Macchina1().change_x : int | float = 0
        Player.Macchina1().change_y : int | float = 0
        Player.Macchina1().change_angle : int | float = 0
        
        if Player.Macchina1().up_pressed:
            if Player.Macchina1().macchina1.angle > 180 or Player.Macchina1().macchina1.angle < -180:
                return print("morto")
            else:
                Player.Macchina1().change_angle -= Player.Macchina1().macchina1_velocita_angle
        if Player.Macchina1().down_pressed:
            if Player.Macchina1().macchina1.angle > 180 or Player.Macchina1().macchina1.angle < -180:
                return print("morto")
            else:
                Player.Macchina1().change_angle += Player.Macchina1().macchina1_velocita_angle
        if Player.Macchina1().left_pressed:
            Player.Macchina1().change_x -= Player.Macchina1().macchina1_velocita
        if Player.Macchina1().right_pressed:
            Player.Macchina1().change_x += Player.Macchina1().macchina1_velocita
        
        


        # Applica movimento
        Player.Macchina1().center_x += Player.Macchina1().change_x
        Player.Macchina1().center_y += Player.Macchina1().change_y
        Player.Macchina1().angle += Player.Macchina1().change_angle

        
       

       



    def on_key_press(self, key, modifiers):
        if key == arcade.key.W or key == arcade.key.UP:
            Player.Macchina1().up_pressed = True
            print("sù")
        elif key == arcade.key.S or key == arcade.key.DOWN:
            Player.Macchina1().down_pressed = True
            print("giù")
        elif key == arcade.key.A or key == arcade.key.LEFT:
            Player.Macchina1().left_pressed = True
            print("indietro")
        elif key == arcade.key.D or key == arcade.key.RIGHT:
            Player.Macchina1().right_pressed = True
            print("avanti")
            

        
    def on_key_release(self, key, modifiers):
        if key == arcade.key.W or key == arcade.key.UP:
            Player.Macchina1().up_pressed = False
            print("non sù")
        elif key == arcade.key.S or key == arcade.key.DOWN:
            Player.Macchina1().down_pressed = False
            print("non giù")
        elif key == arcade.key.A or key == arcade.key.LEFT:
            Player.Macchina1().left_pressed = False
            print("non indietro")
        elif key == arcade.key.D or key == arcade.key.RIGHT:
            Player.Macchina1().right_pressed = False
            print("non avanti")


    def aggiorna_punteggio(self, nuovo_punteggio):
        self.testo_score.text = f"Punteggio: {self.conta_monete_prese}"
        


def main():
    game = MyGame(
        SCREEN_WIDTH, SCREEN_HEIGHT, "Hill Climb Racing"
    )
    arcade.run()


if __name__ == "__main__":
    main()