import arcade
import os
# from arcade import *

class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title, fullscreen=True)

        self.macchina = None
        self.playerSpriteList = arcade.SpriteList()
        

        self.setup()

    def on_draw(self):
        # Pulisci lo schermo
        self.clear()
   

    def setup(self):
        
        self.macchina = arcade.Sprite("./immagini/78614.png")

        self.macchina.center_x = 100
        self.macchina.center_y = 200
        self.macchina.scale_x = 1
        self.macchina.scale_y = 1
        self.macchina.angle = 0

        self.playerSpriteList.append(self.macchina)

    def on_key_press(self, key, modifiers):
            if key == arcade.key.W:
                self.macchina.angle -= 10
            elif key == arcade.key.UP:
                self.macchina.angle -= 10
            elif key == arcade.key.A:
                self.macchina.center_x -= 10
            elif key == arcade.key.LEFT:
                self.macchina.center_x -= 10
            elif key == arcade.key.S:
                self.macchina.angle += 10
            elif key == arcade.key.DOWN:
                self.macchina.angle += 10
            elif key == arcade.key.D:
                self.macchina.center_x += 10
            elif key == arcade.key.RIGHT:
                self.macchina.center_x += 10





    def on_draw(self):
        self.playerSpriteList.draw()
        
    def on_update(self, deltaTime):
        pass




def main():
    game = MyGame(
        600, 600, "Il mio giochino"
    )
    arcade.run()



    
                                     


if __name__ == "__main__":
    main()

