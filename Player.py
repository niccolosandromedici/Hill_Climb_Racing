import arcade

class Macchina1(arcade.Sprite):
    def __init__(self):
        super().__init__()
        #self.gravity : int | float = 1
        self.macchina_list = arcade.SpriteList()
        self.macchina1 = arcade.Sprite("./immagini/78614.png")
        self.macchina1.center_x : int = 100
        self.macchina1.center_y : int = 350
        self.macchina1.scale_x : int = 1
        self.macchina1.scale_y : int = 1
        self.macchina1.angle : int = 0
        self.macchina1_velocita : int | float = 5
        self.macchina1_velocita_angle : int | float = 1
        self.macchina_list.append(self.macchina1)

        self.up_pressed : bool = False
        self.down_pressed : bool = False
        self.left_pressed : bool = False
        self.right_pressed : bool = False

        self.physics_engine = None


    def set_physic_engine(self, engine):
        self.physics_engine = engine

    def setup(self):
        #self.camera = arcade.Camera2D()
        #return super().setup()
        pass

    def on_draw(self):
        self.macchina_list.draw()
        #self.camera.use()
        #return super().on_draw()
        
    
    def on_update(self, delta_time):
        #self.physics_engine.update()

        #movimento camera
        #self.camera.position = self.macchina1.position
        
       


    #     self.change_x : int | float = 0
    #     self.change_y : int | float = 0
    #     self.change_angle : int | float = 0

    #     if self.up_pressed:
    #         if self.macchina1.angle > 180 or self.macchina1.angle < -180:
    #             return print("morto")
    #         else:
    #             self.change_angle -= self.macchina1_velocita_angle
    #     if self.down_pressed:
    #         if self.macchina1.angle > 180 or self.macchina1.angle < -180:
    #             return print("morto")
    #         else:
    #             self.change_angle += self.macchina1_velocita_angle
    #     if self.left_pressed:
    #         self.change_x -= self.macchina1_velocita
    #     if self.right_pressed:
    #         self.change_x += self.macchina1_velocita


    #     self.macchina1.center_x += self.change_x
    #     self.macchina1.center_y += self.change_y
    #     self.macchina1.angle += self.change_angle


    # def on_key_press(self, key, modifiers):
    #     if key == arcade.key.W or key == arcade.key.UP:
    #         self.up_pressed = True
    #     elif key == arcade.key.S or key == arcade.key.DOWN:
    #         self.down_pressed = True
    #     elif key == arcade.key.A or key == arcade.key.LEFT:
    #         self.left_pressed = True
    #     elif key == arcade.key.D or key == arcade.key.RIGHT:
    #         self.right_pressed = True
    #     #elif key == arcade.key.SPACE:  
    #         #if self.physics_engine.can_jump():
    #             #self.macchina1.change_y = self.jump_speed

    # def on_key_release(self, key, modifiers):
    #     if key == arcade.key.W or key == arcade.key.UP:
    #         self.up_pressed = False
    #     elif key == arcade.key.S or key == arcade.key.DOWN:
    #         self.down_pressed = False
    #     elif key == arcade.key.A or key == arcade.key.LEFT:
    #         self.left_pressed = False
    #     elif key == arcade.key.D or key == arcade.key.RIGHT:
    #         self.right_pressed = False
    
        pass



