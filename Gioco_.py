import arcade
import os
import random

#https://api.arcade.academy/en/stable/tutorials/platform_tutorial/step_07.html
#sito con tutta la documentazione necessaria per il mio gioco


class MyGame(arcade.Window):
    SCREEN_WIDTH : int = 900
    SCREEN_HEIGHT : int = 600
    MONETA_WIDTH : int = 32
    MONETA_HEIGHT : int = 32
    

    def __init__(self, width, height, title, ):
        super().__init__(width, height, title, fullscreen = False)

        self.macchina_list = arcade.SpriteList()
        self.moneta_list = arcade.SpriteList()
        
        #suono
        self.suono_motore = arcade.load_sound("./immagini/audio_motore.mp3")
        #scala
        self.tile_scaling : int | float = 0.5
        #fisica
        self.gravity : int | float = 1
        #self.jump_speed : int | float = 20

        #movimento
        self.velocita : int | float = 4
        self.velocita_angle : int| float = 1
        
        #conta monete
        self.conta_monete_prese : int = 0

        self.testo_score : str | bool = None

        self.setup()

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.up_pressed : bool = False
        self.down_pressed : bool = False
        self.left_pressed : bool = False
        self.right_pressed : bool = False

        
        # SpriteList for our boxes and ground
        # Putting our ground and box Sprites in the same SpriteList
        # will make it easier to perform collision detection against
        # them later on. Setting the spatial hash to True will make
        # collision detection much faster if the objects in this
        # SpriteList do not move.
        self.wall_list = arcade.SpriteList(use_spatial_hash = True)

        # Create the ground
        # This shows using a loop to place multiple sprites horizontally
        for x in range(-10000, 10000, 64):
            ground = arcade.Sprite(":resources:images/tiles/grassMid.png", scale = self.tile_scaling)
            ground.center_x = x
            ground.center_y = 250
            self.wall_list.append(ground)

        # Create a Platformer Physics Engine.
        # This will handle moving our player as well as collisions between
        # the player sprite and whatever SpriteList we specify for the walls.
        # It is important to supply static platforms to the walls parameter. There is a
        # platforms parameter that is intended for moving platforms.
        # If a platform is supposed to move, and is added to the walls list,
        # it will not be moved.
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.macchina, walls = self.wall_list, gravity_constant = self.gravity)

        

    def setup(self):
        
        self.macchina = arcade.Sprite("./immagini/78614.png")
        self.macchina.center_x : int = 100
        self.macchina.center_y : int = 250
        self.macchina.scale_x : int = 1
        self.macchina.scale_y : int = 1
        self.macchina.angle : int = 0
        self.macchina_list.append(self.macchina)

        #crea monete iniziali
        for i in range(5):
            self.crea_monete(tipo = "oro")
        self.crea_monete(tipo = "diamante")

        # Set up the camera
        self.camera = arcade.Camera2D()
        

        #carica sfondo
        self.background = arcade.load_texture("immagini/Sfondo.jpg")
        

        #scrivi testo punteggio
        self.testo_score = arcade.Text( #testo del punteggio
            text="Punteggio: " + str(self.conta_monete_prese),
            x = self.macchina.center_x, # Centro dello schermo
            y = self.macchina.center_y + 350, # Vicino in alto
            color = arcade.color.BLACK,
            font_size = 24,
            font_name = "Arial", # O il nome del tuo font caricato
            anchor_x = "center" # Allinea il testo a sinistra
        )

    
    def crea_monete(self, tipo):

        print("[" + str(self.conta_monete_prese) + "] == > Creazione monete...")


        next_x = self.macchina.center_x

        while abs(next_x - self.macchina.center_x) < 100 :
            next_x = (MyGame.MONETA_WIDTH/2) + (self.macchina.center_x + random.randint(100, (MyGame.SCREEN_WIDTH - MyGame.MONETA_WIDTH)))%(MyGame.SCREEN_WIDTH - MyGame.MONETA_WIDTH)

        next_y = self.macchina.center_y + 80

        # while abs(next_y - self.macchina.center_y) < 100 :
        #     next_y = (MyGame.MONETA_HEIGHT/2) + (self.macchina.center_y + random.randint(100, (MyGame.SCREEN_HEIGHT - MyGame.MONETA_HEIGHT)))%(MyGame.SCREEN_HEIGHT - MyGame.MONETA_HEIGHT)

        print("[",self.macchina.center_x,"][", self.macchina.center_y,"] = > moneta creata in: [",next_x, "] [", next_y, "]")


        

        if tipo == "oro":
            self.moneta = arcade.Sprite("./immagini/moneta.jpg")
            self.moneta.center_x = next_x
            self.moneta.center_y = next_y
            self.moneta.scale = 0.2
            self.moneta.tipo = "oro"
            self.moneta_list.append(self.moneta)

        if tipo == "diamante":
            pass
            # Implementare altri tipi di monete o oggetti se necessario

        
    def rimuovi_moneta(self, Sprite_moneta):
        Sprite_moneta.remove_from_sprite_lists()
        #print("Moneta scomparsa!")
    #def rimuovi_diamante(self, Sprite_moneta):
       #     Sprite_moneta.remove_from_sprite_lists()
       #     #print("Golden Cookie scomparso!")




    def on_draw(self):
        self.clear()

        arcade.draw_texture_rect(self.background, arcade.types.Viewport( self.camera.position[0] - MyGame.SCREEN_WIDTH/2, self.camera.position[1] - MyGame.SCREEN_HEIGHT/3.2, MyGame.SCREEN_WIDTH + 100, MyGame.SCREEN_HEIGHT + 100) )

        self.macchina_list.draw()
        self.moneta_list.draw()

        self.wall_list.draw()
        self.camera.use()
        self.testo_score.draw()
    



    def on_update(self, deltaTime):
        
        self.physics_engine.update()
        
        #movimento camera
        self.camera.position = self.macchina.position
        

        # Calcola movimento in base ai tasti premuti
        change_x : int | float = 0
        change_y : int | float = 0
        change_angle : int | float = 0
        
        if self.up_pressed:
            change_angle -= self.velocita_angle
        if self.down_pressed:
            change_angle += self.velocita_angle
        if self.left_pressed:
            change_x -= self.velocita
        if self.right_pressed:
            change_x += self.velocita
        
        # Applica movimento
        self.macchina.center_x += change_x
        self.macchina.center_y += change_y
        self.macchina.angle += change_angle

    def on_key_press(self, key, modifiers):
        if key == arcade.key.W or key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.S or key == arcade.key.DOWN:
            self.down_pressed = True
        elif key == arcade.key.A or key == arcade.key.LEFT:
            self.left_pressed = True
            #if not self.suono_motore.is_playing:
            #    arcade.play_sound(self.suono_motore)
        elif key == arcade.key.D or key == arcade.key.RIGHT:
            self.right_pressed = True
            #if not self.suono_motore.is_playing:
            #    arcade.play_sound(self.suono_motore)
        #elif key == arcade.key.SPACE:  
        #    if self.physics_engine.can_jump():
        #        self.macchina.change_y = self.jump_speed




    def on_key_release(self, key, modifiers):
        if key == arcade.key.W or key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.S or key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.A or key == arcade.key.LEFT:
            self.left_pressed = False
            #if self.suono_motore.is_playing:
            #    arcade.stop_sound(self.suono_motore)
        elif key == arcade.key.D or key == arcade.key.RIGHT:
            self.right_pressed = False
            #if self.suono_motore.is_playing:
            #    arcade.stop_sound(self.suono_motore)
            



         # Gestione collisioni
        collisioni = arcade.check_for_collision_with_list(self.macchina, self.moneta_list)        
        if len(collisioni) > 0: # Vuol dire che il personaggio si è scontrato con qualcosa
            if collisioni[0].tipo == "oro":
                self.conta_monete_prese += 1
                self.testo_score.text = f"Punteggio: {self.conta_monete_prese}"
                collisioni[0].remove_from_sprite_lists()
                self.crea_monete(tipo = "oro")
                #print("moneta presa! Punteggio:", self.conta_monete_prese)

            #da implementare con dei diamanti o altro
            # elif collisioni[0].tipo == "golden":
            #     self.conta_monete_prese += 100
            #     self.testo_score.text = f"Punteggio: {self.conta_monete_prese}"
            #     collisioni[0].remove_from_sprite_lists()
            #     self.crea_monete(tipo = "diamante")
            #     #print("Golden Biscotto mangiato! Punteggio:", self.conta_monete_prese)
           
            




        # # Limita movimento dentro lo schermo
        # if self.macchina.center_x < 0:
        #       self.macchina.center_x = 0
        # elif self.macchina.center_x > self.width:
        #       self.macchina.center_x = self.width

        # if self.macchina.center_y < 0:
        #       self.macchina.center_y = 0
        # elif self.macchina.center_y > self.height:
        #       self.macchina.center_y = self.height

    def aggiorna_punteggio(self, nuovo_punteggio):
        self.testo_score.text = f"Punteggio: {self.conta_monete_prese}"
        


def main():
    game = MyGame(
        MyGame.SCREEN_WIDTH, MyGame.SCREEN_HEIGHT, "Hill Climb Racing"
    )
    arcade.run()


if __name__ == "__main__":
    main()

