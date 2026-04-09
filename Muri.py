import arcade
import math



class Muri_(arcade.Sprite):
    def __init__(self):
        super().__init__()

        #scala
        self.tile_scaling : int | float = 0.5

        #lista muri
        self.wall_list = arcade.SpriteList(use_spatial_hash = True)

        #pavimento
        for x in range(-350, 2000, 10):
            ground = arcade.Sprite(":resources:images/tiles/grassMid.png", scale = self.tile_scaling)
            ground.center_x = x
            ground.center_y = 200 + math.sin(x / 100) * 50 # terreno ondulato
            self.wall_list.append(ground)
        
        #muro verticale
        for y in range(200, 700, 70):
            start_wall = arcade.Sprite(":resources:images/tiles/grassMid.png", scale = self.tile_scaling)
            start_wall.center_x = -385
            start_wall.center_y = y
            self.wall_list.append(start_wall)  


            


    