#Testeo del modulo arcade

import arcade

#Constantes de dibuji
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_TITLE = "HUEVOSSSS"
RADIUS = 150
SCALING = 2.0

class UnoGame(arcade.Window):
    """
    CLase para juego UNO
    """
    def __init__(self, width, height, title, fullscreen=False, resizable=False, update_rate=1 /60, antialiasing=True):
        super().__init__(width=width, height=height, title=title, fullscreen=fullscreen, resizable=resizable, update_rate=update_rate, antialiasing=antialiasing)
        #Definir sprites de las cartas.
        self.lista_cartas = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()

    def setup(self):
        """
        Preparar el juego para jugar.
        """
        #Poner un color de fondo.
        arcade.set_background_color(arcade.color.SKY_BLUE)

        #Configurar Mazo
        for num in range(0,108):
            carta = arcade.Sprite("images/UNO-Card_"+num+".png",SCALING)
            carta.center_y = self.height / 2
            carta.left = 10
            self.all_sprites.append(carta)



#ABRIR UNA VENTANA:
arcade.open_window(SCREEN_HEIGHT,SCREEN_HEIGHT,SCREEN_TITLE)

#poner un color de fondo
arcade.set_background_color(arcade.color.WHITE)

#CLear the screen and start drawing
arcade.start_render()

#dibujar un circulo
arcade.draw_circle_filled(
    SCREEN_WIDTH/2, SCREEN_HEIGHT/2, RADIUS, arcade.color.BLUE
)

#Terminar el renderizado
arcade.finish_render()

#Mostrar todo
arcade.run()