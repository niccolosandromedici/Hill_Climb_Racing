import arcade
import os


#https://api.arcade.academy/en/stable/tutorials/platform_tutorial/step_07.html
#sito con tutta la documentazione necessaria per il mio gioco


class MyGame(arcade.Window):
    SCREEN_WIDTH : int = 900
    SCREEN_HEIGHT : int = 600
    

    def __init__(self, width, height, title, ):
        super().__init__(width, height, title, fullscreen = False)

        self.macchina = None
        self.playerSpriteList = arcade.SpriteList()
        #suono
        self.suono_motore = arcade.load_sound("./immagini/audio_motore.mp3")
        #scala
        self.tile_scaling : int | float = 0.5
        #fisica
        self.gravity : int | float = 1
        self.jump_speed : int | float = 20

        #movimento
        self.velocita : int | float = 4
        self.velocita_angle : int| float = 1
        

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

        self.camera = arcade.Camera2D()
        

        self.playerSpriteList.append(self.macchina)
        
        self.background = arcade.load_texture("immagini/Sfondo.jpg")
            

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rect(self.background, arcade.types.Viewport( self.camera.position[0] - MyGame.SCREEN_WIDTH/2, self.camera.position[1] - MyGame.SCREEN_HEIGHT/3.2, MyGame.SCREEN_WIDTH + 100, MyGame.SCREEN_HEIGHT + 100) )

        self.playerSpriteList.draw()
        self.wall_list.draw()
        self.camera.use()

    
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
            #arcade.play_sound(self.suono_motore)
        elif key == arcade.key.D or key == arcade.key.RIGHT:
            self.right_pressed = True
            #arcade.play_sound(self.suono_motore)
        elif key == arcade.key.SPACE:  
            if self.physics_engine.can_jump():
                self.macchina.change_y = self.jump_speed




    def on_key_release(self, key, modifiers):
        if key == arcade.key.W or key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.S or key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.A or key == arcade.key.LEFT:
            self.left_pressed = False
            #self.suono_motore.set_volume(0.0)
        elif key == arcade.key.D or key == arcade.key.RIGHT:
            self.right_pressed = False
            #self.suono_motore.set_volume(0.0)

        # # Limita movimento dentro lo schermo
        # if self.macchina.center_x < 0:
        #       self.macchina.center_x = 0
        # elif self.macchina.center_x > self.width:
        #       self.macchina.center_x = self.width

        # if self.macchina.center_y < 0:
        #       self.macchina.center_y = 0
        # elif self.macchina.center_y > self.height:
        #       self.macchina.center_y = self.height
        


def main():
    game = MyGame(
        MyGame.SCREEN_WIDTH, MyGame.SCREEN_HEIGHT, "Hill Climb Racing"
    )
    arcade.run()


if __name__ == "__main__":
    main()

