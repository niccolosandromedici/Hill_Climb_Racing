import arcade
from Muri import Muri_
# from GameOver import GameOver_

class Macchina(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.gravity : int | float = 1
        self.macchina_list = arcade.SpriteList()
        self.up_pressed : bool = False
        self.down_pressed : bool = False
        self.left_pressed : bool = False
        self.right_pressed : bool = False

        self.setup()
                
    def setup(self):
        # Set up the camera
        self.camera = arcade.Camera2D()

    def on_draw(self):
        self.camera.use()
        self.macchina_list.draw()

    def on_update(self, delta_time):
        self.physics_engine.update()

    # def on_key_press(self, key, modifiers):
    #     if key == arcade.key.W or key == arcade.key.UP:
    #         self.up_pressed = True
    #     elif key == arcade.key.S or key == arcade.key.DOWN:
    #         self.down_pressed = True
    #     elif key == arcade.key.A or key == arcade.key.LEFT:
    #         self.left_pressed = True
    #         #if not self.suono_motore.is_playing:
    #         #    arcade.play_sound(self.suono_motore)
    #     elif key == arcade.key.D or key == arcade.key.RIGHT:
    #         self.right_pressed = True
    #         #if not self.suono_motore.is_playing:
    #         #    arcade.play_sound(self.suono_motore)
    #     #elif key == arcade.key.SPACE:  
    #     #    if self.physics_engine.can_jump():
    #     #        self.macchina1.change_y = self.jump_speed

    # def on_key_release(self, key, modifiers):
    #     if key == arcade.key.W or key == arcade.key.UP:
    #         self.up_pressed = False
    #     elif key == arcade.key.S or key == arcade.key.DOWN:
    #         self.down_pressed = False
    #     elif key == arcade.key.A or key == arcade.key.LEFT:
    #         self.left_pressed = False
    #         #if self.suono_motore.is_playing:
    #         #    arcade.stop_sound(self.suono_motore)
    #     elif key == arcade.key.D or key == arcade.key.RIGHT:
    #         self.right_pressed = False
    #         #if self.suono_motore.is_playing:
    #         #    arcade.stop_sound(self.suono_motore)
        

class Macchina1(Macchina):
    def __init__(self):
        super().__init__()
        self.macchina1 = arcade.Sprite("./immagini/78614.png")
        self.macchina1.center_x : int = 100
        self.macchina1.center_y : int = 250
        self.macchina1.scale_x : int = 1
        self.macchina1.scale_y : int = 1
        self.macchina1.angle : int = 0
        self.macchina1_velocita : int | float = 5
        self.macchina1_velocita_angle : int | float = 1
        self.macchina_list.append(self.macchina1)

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.macchina1, walls = Muri_().wall_list, gravity_constant = self.gravity)
    


    def setup(self):
        return super().setup()

    def on_draw(self):
        return super().on_draw()
    
    def on_update(self, delta_time):

        #movimento camera
        self.camera.position = self.macchina1.position
       


        self.change_x : int | float = 0
        self.change_y : int | float = 0
        self.change_angle : int | float = 0

        if self.up_pressed:
            if self.macchina1.angle > 180 or self.macchina1.angle < -180:
                return print("morto")
            else:
                self.change_angle -= self.macchina1_velocita_angle
        if self.down_pressed:
            if self.macchina1.angle > 180 or self.macchina1.angle < -180:
                return print("morto")
            else:
                self.change_angle += self.macchina1_velocita_angle
        if self.left_pressed:
            self.change_x -= self.macchina1_velocita
        if self.right_pressed:
            self.change_x += self.macchina1_velocita


        self.macchina1.center_x += self.change_x
        self.macchina1.center_y += self.change_y
        self.macchina1.angle += self.change_angle

    
    



class Macchina2(Macchina):
    def __init__(self):
        super().__init__(Macchina)
        self.macchina2 = arcade.Sprite("./immagini/Car_blue.png")
        self.macchina2.center_x : int = 100
        self.macchina2.center_y : int = 250
        self.macchina2.scale_x : int = 1
        self.macchina2.scale_y : int = 1
        self.macchina2.angle : int = 0
        self.macchina2_velocita : int | float = 7
        self.macchina2_velocita_angle : int | float = 2
        self.macchina_list.append(self.macchina2)

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.macchina2, walls = Muri_().wall_list, gravity_constant = self.gravity)
    
    def setup(self):
        return super().setup()

    def on_draw(self):
        return super().on_draw()

    def on_update(self, delta_time):
        #movimento camera
        self.camera.position = self.macchina2.position
        

        self.change_x : int | float = 0
        self.change_y : int | float = 0
        self.change_angle : int | float = 0

        if self.up_pressed:
            if self.macchina2.angle > 180 or self.macchina2.angle < -180:
                return print("morto")
            else:
                self.change_angle -= self.macchina2_velocita_angle
        if self.down_pressed:
            if self.macchina2.angle > 180 or self.macchina2.angle < -180:
                return print("morto")
            else:
                self.change_angle += self.macchina2_velocita_angle
        if self.left_pressed:
            self.change_x -= self.macchina2_velocita
        if self.right_pressed:
            self.change_x += self.macchina2_velocita


        self.macchina2.center_x += self.change_x
        self.macchina2.center_y += self.change_y
        self.macchina2.angle += self.change_angle
        
    


class Macchina3(Macchina):
    def __init__(self):
        super().__init__(Macchina)
        self.macchina3 = arcade.Sprite("./immagini/Car_red.png")
        self.macchina3.center_x : int = 100
        self.macchina3.center_y : int = 250
        self.macchina3.scale_x : int = 1
        self.macchina3.scale_y : int = 1
        self.macchina3.angle : int = 0
        self.macchina3_velocita : int | float = 9
        self.macchina3_velocita_angle : int | float = 3
        self.macchina_list.append(self.macchina3)

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.macchina3, walls = Muri_().wall_list, gravity_constant = self.gravity)

    def setup(self):
        return super().setup()

    def on_draw(self):
        return super().on_draw()

    def on_update(self, delta_time):
        #movimento camera
        self.camera.position = self.macchina3.position
       

        self.change_x : int | float = 0
        self.change_y : int | float = 0
        self.change_angle : int | float = 0

        if self.up_pressed:
            if self.macchina3.angle > 180 or self.macchina3.angle < -180:
                return print("morto")
            else:
                self.change_angle -= self.macchina3_velocita_angle
        if self.down_pressed:
            if self.macchina3.angle > 180 or self.macchina3.angle < -180:
                return print("morto")
            else:
                self.change_angle += self.macchina3_velocita_angle
        if self.left_pressed:
            self.change_x -= self.macchina3_velocita
        if self.right_pressed:
            self.change_x += self.macchina3_velocita


        self.macchina3.center_x += self.change_x
        self.macchina3.center_y += self.change_y
        self.macchina3.angle += self.change_angle


    
        