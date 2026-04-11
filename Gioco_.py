import arcade
import os
import random
from Muri import Muri_
from GameOver import GameOver_
from win_screen import WinScreen_
from Pausa import PauseView




class MyGame(arcade.View):

    SCREEN_WIDTH   = 900
    SCREEN_HEIGHT   = 600
    COLLEZIONABILI_WIDTH   = 32
    COLLEZIONABILI_HEIGHT   = 32
    

    def __init__(self):
        
        super().__init__()

        #lista macchine e collezzionabili
        self.macchina_list = arcade.SpriteList()
        self.collezzionabili_list = arcade.SpriteList()
        
        #scala
        self.tile_scaling = 0.5

        #fisica
        self.gravity = 1
        self.jump_speed = 20

        #movimento
        self.velocita = 5
        self.velocita_angle = 2.5
        
        #conta monete e diamanti
        self.conta_monete_prese   = 0
        self.conta_diamanti_presi   = 0

        #testo punteggio
        self.testo_score_monete = None
        self.testo_score_diamanti = None


        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        #tasti premuti
        self.up_pressed = False
        self.down_pressed = False
        self.left_pressed = False
        self.right_pressed = False

        #stato del gioco
        self.vincitore = False
        self.morto = False
        self.game_over = GameOver_()
        self.win_screen = WinScreen_()
        self.wait = PauseView(self)



        self.setup()

        #fisica
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.macchina1, walls = Muri_().wall_list, gravity_constant = self.gravity)
       
        
        

    def setup(self):

        #crea macchina
        self.crea_macchina()

        #crea collezzionabili iniziali
        for i in range(5):
            self.crea_collezzionabili(tipo = "oro")
        self.crea_collezzionabili(tipo = "diamante")

        # Set up the camera
        self.camera = arcade.Camera2D()
        

        #carica sfondo
        self.background = arcade.load_texture("immagini/Sfondo.jpg")
        

        #scrivi testo punteggio delle monete
        self.testo_score_monete = arcade.Text( #testo del punteggio
            text="Monete: " + str(self.conta_monete_prese),
            x = self.macchina1.center_x,
            y = self.macchina1.center_y + 300,
            color = arcade.color.BLACK,
            font_size = 24,
            font_name = "Arial", # O il nome del tuo font caricato
            anchor_x = "center" # Allinea il testo a sinistra
        )

        #scrivi testo punteggio dei diamanti
        self.testo_score_diamanti = arcade.Text( #testo del punteggio
            text="Diamanti: " + str(self.conta_diamanti_presi),
            x = self.macchina1.center_x,
            y = self.macchina1.center_y + 250, 
            color = arcade.color.BLACK,
            font_size = 24,
            font_name = "Arial", # O il nome del tuo font caricato
            anchor_x = "center" # Allinea il testo a sinistra
        )

        

    #crea macchina
    def crea_macchina(self):
        self.macchina1 = arcade.Sprite("./immagini/78614.png")
        self.macchina1.center_x = 100
        self.macchina1.center_y = 250
        self.macchina1.scale_x = 1
        self.macchina1.scale_y = 1
        self.macchina1.angle = 0
        self.velocita = 10
        self.velocita_angle = 2.5
        self.macchina_list.append(self.macchina1)
       


    #crea collezzionabili
    def crea_collezzionabili(self, tipo):

        #print("[" + str(self.conta_monete_prese) + "] == > Creazione monete...")

        next_x = self.macchina1.center_x

        while abs(next_x - self.macchina1.center_x) < 100 :
            next_x = ((MyGame.COLLEZIONABILI_HEIGHT/2) + (self.macchina1.center_x + random.randint(100, (MyGame.SCREEN_WIDTH - MyGame.COLLEZIONABILI_WIDTH)))%(MyGame.SCREEN_WIDTH - MyGame.COLLEZIONABILI_WIDTH)) + self.macchina1.center_x + 1000

        next_y  = random.randint(300, 400)

        #print("[",self.macchina1.center_x,"][", self.macchina1.center_y,"] = > moneta creata in: [",next_x, "] [", next_y, "]")

        if tipo == "oro":
            self.moneta = arcade.Sprite("./immagini/Moneta_senza_sfondo.png")
            self.moneta.center_x = next_x
            self.moneta.center_y = next_y
            self.moneta.scale = 0.2
            self.moneta.tipo = "oro"
            self.collezzionabili_list.append(self.moneta)

        if tipo == "diamante":
            self.moneta = arcade.Sprite("./immagini/Diamante.png")
            self.moneta.center_x = next_x
            self.moneta.center_y = next_y
            self.moneta.scale = 0.2
            self.moneta.tipo = "diamante"
            self.collezzionabili_list.append(self.moneta)

    #rimuovi collezzionabili
    def rimuovi_moneta(self, Sprite_moneta):
        Sprite_moneta.remove_from_sprite_lists()
        #print("Moneta scomparsa!")
    def rimuovi_diamante(self, Sprite_moneta):
        Sprite_moneta.remove_from_sprite_lists()
        #print("Diamante scomparso!")




    def on_draw(self):
        #pulisco lo schermo
        self.clear()

        #disegno lo sfondo
        arcade.draw_texture_rect(self.background,
                                arcade.types.Viewport(
                                self.camera.position[0] - MyGame.SCREEN_WIDTH/2,
                                -100,
                                MyGame.SCREEN_WIDTH + 100,
                                MyGame.SCREEN_HEIGHT + 400) 
                                )
        
        #disegno macchine, collezzionabili e muri
        self.macchina_list.draw()
        self.collezzionabili_list.draw()
        Muri_().wall_list.draw()
        
        #applico la camera
        self.camera.use()

        #disegno il testo del punteggio
        self.testo_score_monete.draw()
        self.testo_score_diamanti.draw()

        #disegno schermata di game over/vittoria/pausa se necessario
        if self.morto == True:
            self.clear()    
            self.game_over.on_draw()

        if self.vincitore == True:
            self.clear()
            self.win_screen.on_draw()     




    def on_update(self, deltaTime):
        
        
        #aggiorna fisica
        self.physics_engine.update()
        
        #movimento camera con morto
        if self.morto == False:
            self.camera.position = self.macchina1.position
        else:
            self.camera.position = (1000, 1000)

        #movimento camera con vincitore
        if self.macchina1.center_x >= 1990:
            self.vincitore = True
        if self.vincitore == True:
            self.camera.position = (1000, 1000)

        # Calcola movimento in base ai tasti premuti
        change_x = 0
        change_y = 0
        change_angle = 0
        
        if self.up_pressed:
            if (self.macchina1.angle > 180 or self.macchina1.angle < -180) and self.morto == False:
                self.morto = True
            else:
                change_angle -= self.velocita_angle
        if self.down_pressed:
            if (self.macchina1.angle > 180 or self.macchina1.angle < -180) and self.morto == False:
                self.morto = True   
            else:
                change_angle += self.velocita_angle
        if self.left_pressed:
            if (self.macchina1.angle > 180 or self.macchina1.angle < -180) and self.morto == False:
                self.morto = True
            else:
                change_x -= self.velocita
        if self.right_pressed:
            if (self.macchina1.angle > 180 or self.macchina1.angle < -180) and self.morto == False:
                self.morto = True
            else:   
                change_x += self.velocita

        # Gestione collisioni tra macchina e collezionabili
        collisioni_macchina_collezzionabili = arcade.check_for_collision_with_list(self.macchina1, self.collezzionabili_list)       

        if len(collisioni_macchina_collezzionabili) > 0: # Vuol dire che il personaggio si è scontrato con qualcosa

            if collisioni_macchina_collezzionabili[0].tipo == "oro":
                self.conta_monete_prese += 1
                self.testo_score_monete.text = f"Monete: {self.conta_monete_prese}"
                collisioni_macchina_collezzionabili[0].remove_from_sprite_lists()
                self.crea_collezzionabili(tipo = "oro")
                #print("moneta presa! Punteggio:", self.conta_monete_prese)

            elif collisioni_macchina_collezzionabili[0].tipo == "diamante":
                self.conta_diamanti_presi += 1
                self.testo_score_diamanti.text = f"Diamanti: {self.conta_diamanti_presi}"
                collisioni_macchina_collezzionabili[0].remove_from_sprite_lists()
                self.crea_collezzionabili(tipo = "diamante")
                #print("Diamante preso! Punteggio:", self.conta_diamanti_presi)



        # Applica movimento
        self.macchina1.center_x += change_x
        self.macchina1.center_y += change_y
        self.macchina1.angle += change_angle

        #aggiornamento x delle scritte
        self.testo_score_monete.x += change_x
        self.testo_score_diamanti.x += change_x
       
       



    def on_key_press(self, key, modifiers):
        if key == arcade.key.W or key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.S or key == arcade.key.DOWN:
            self.down_pressed = True
        elif key == arcade.key.A or key == arcade.key.LEFT:  
            self.left_pressed = True
        elif key == arcade.key.D or key == arcade.key.RIGHT:      
            self.right_pressed = True
        elif key == arcade.key.ESCAPE:
            self.close()
        elif key == arcade.key.R:
                if self.morto == True or self.vincitore == True:
                    self.morto = False
                    self.vincitore = False
                self.macchina1.center_x = 100
                self.macchina1.center_y = 250
                self.macchina1.angle = 0
                self.testo_score_monete.x = self.macchina1.center_x
                self.testo_score_diamanti.x = self.macchina1.center_x
                self.conta_monete_prese = 0
                self.conta_diamanti_presi = 0
                self.testo_score_monete.text = f"Monete: {self.conta_monete_prese}"
                self.testo_score_diamanti.text = f"Diamanti: {self.conta_diamanti_presi}"
        elif key == arcade.key.P:
            pausa = PauseView(self)
            self.window.show_view(pausa)
        elif key == arcade.key.SPACE:  
            if self.physics_engine.can_jump():
                self.macchina1.change_y = self.jump_speed
                




    def on_key_release(self, key, modifiers):
        if key == arcade.key.W or key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.S or key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.A or key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.D or key == arcade.key.RIGHT:
            self.right_pressed = False
            
      



    def aggiorna_punteggio(self, nuovo_punteggio):
        self.testo_score.text = f"Punteggio: {self.conta_monete_prese}"
        



