import arcade
import Player
import Gioco_


class Muri_(arcade.Sprite):
    def __init__(self):
        super().__init__()

        #scala
        self.tile_scaling : int | float = 0.5

        # SpriteList for our boxes and ground
        # Putting our ground and box Sprites in the same SpriteList
        # will make it easier to perform collision detection against
        # them later on. Setting the spatial hash to True will make
        # collision detection much faster if the objects in this
        # SpriteList do not move.
        self.wall_list = arcade.SpriteList(use_spatial_hash = True)

        # Create the ground
        # This shows using a loop to place multiple sprites horizontally
        for x in range(-350, 1000, 64):
            ground = arcade.Sprite(":resources:images/tiles/grassMid.png", scale = self.tile_scaling)
            ground.center_x = x
            ground.center_y = 250
            #ground.angle = random.randint(0, 180)
            self.wall_list.append(ground)
        

        for y in range(-10000, 10, 64):
            start_wall = arcade.Sprite(":resources:images/tiles/grassMid.png", scale = self.tile_scaling)
            start_wall.center_x = -385
            start_wall.center_y = y
            self.wall_list.append(start_wall)  

    def draw(self):
        self.wall_list.draw()