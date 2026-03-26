import arcade
import arcade.future.background as background


SCREEN_WIDTH : int = 900
SCREEN_HEIGHT : int = 600
CAMERA_SPEED = 0.1


class parallax(arcade.View):
    def __init__(self):
        super().__init__()
        self.background_color = (162, 84, 162, 255)
        self.camera = arcade.Camera2D()

        # Creiamo il gruppo che gestirà tutti i layer
        self.backgrounds = background.ParallaxGroup()

        bg_size = (SCREEN_WIDTH, SCREEN_HEIGHT)

        # Aggiungiamo i layer dal più lontano al più vicino.
        # depth alto = lontano = scorre lento
        self.backgrounds.add_from_file("./immagini/Sfondo_cielo.jpg",    size=bg_size, depth=5.0)
        
        self.backgrounds.add_from_file("./immagini/Sfondo_STRADA.png",   size=(SCREEN_WIDTH, 67), depth=2.0)
        

        self.player = arcade.Sprite("./immagini/78614.png")
        self.player.bottom = 250 # mette il giocatore in basso
        self.x_velocity = 0 # usata per la gestione del movimento, per spostare il giocatore

    def on_draw(self):
        self.clear() # pulisco lo schermo
        self.camera.use()

        bg = self.backgrounds

        # Sposta i layer simulando la profondità
        bg.offset = self.camera.bottom_left
        # Segue la camera per simulare un "mondo infinito"
        bg.pos = self.camera.bottom_left

        bg.draw()
        arcade.draw_sprite(self.player)

    def pan_camera_to_player(self):
        # La camera segue il giocatore in modo "smooth" (lerp). Guarda l'altro blog sulla camera
        self.camera.position = arcade.math.lerp_2d(
            self.camera.position,
            (self.player.center_x, self.height // 2),
            CAMERA_SPEED
        )

    def on_update(self, delta_time: float):
        self.player.center_x += self.x_velocity * delta_time
        self.pan_camera_to_player()