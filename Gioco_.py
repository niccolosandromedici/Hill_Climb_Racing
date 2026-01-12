import arcade
import os
import random



class MyGame(arcade.Window):
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 700

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.macchina = None
        self.playerSpriteList = arcade.SpriteList()
        
        self.velocita = 4
        self.velocita_angle = 1
        

        self.setup()

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.up_pressed = False
        self.down_pressed = False
        self.left_pressed = False
        self.right_pressed = False

       
   


    def setup(self):
        
        self.macchina = arcade.Sprite("./immagini/78614.png")

        self.macchina.center_x = 100
        self.macchina.center_y = 200
        self.macchina.scale_x = 1
        self.macchina.scale_y = 1
        self.macchina.angle = 0

        self.playerSpriteList.append(self.macchina)
        
        self.background = arcade.load_texture("immagini/Immagine sfondo.png")
            

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rect(self.background, arcade.types.Viewport( 0, 0, MyGame.SCREEN_WIDTH, MyGame.SCREEN_HEIGHT) )



        self.playerSpriteList.draw()

    
    def on_update(self, deltaTime):
        

        # Calcola movimento in base ai tasti premuti
        change_x = 0
        change_y = 0
        change_angle = 0
        
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
        elif key == arcade.key.D or key == arcade.key.RIGHT:
            self.right_pressed = True


    def on_key_release(self, key, modifiers):
        if key == arcade.key.W or key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.S or key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.A or key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.D or key == arcade.key.RIGHT:
            self.right_pressed = False

        #  # Limita movimento dentro lo schermo
        # if self.macchina.center_x < 0:
        #      self.macchina.center_x = 0
        # elif self.macchina.center_x > self.width:
        #      self.macchina.center_x = self.width

        # if self.macchina.center_y < 0:
        #      self.macchina.center_y = 0
        # elif self.macchina.center_y > self.height:
        #      self.macchina.center_y = self.height
        


def main():
    game = MyGame(
        MyGame.SCREEN_WIDTH, MyGame.SCREEN_HEIGHT, "Hill Climb Racing"
    )
    arcade.run()


if __name__ == "__main__":
    main()

