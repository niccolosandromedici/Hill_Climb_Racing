import arcade
from Menu import MenuView

class Gioco(arcade.Window):
    def __init__(self):
        super().__init__(900, 600, "Hill Climb Racing")

        menu = MenuView()
        self.show_view(menu)



def main():
    window = Gioco()
    arcade.run()

main()