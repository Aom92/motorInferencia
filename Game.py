#Testeo del modulo arcade

import arcade
import os
from Mazo import Mazo

#Constantes de dibuji
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_TITLE = "HUEVOSSSS"
RADIUS = 150

#Constantes para las cartas
CARD_SCALE = 0.6

#Que tan grande son las cartas
CARD_WIDTH = 140 * CARD_SCALE
CARD_HEIGHT = 140 * CARD_SCALE

#Que tan grande es el tapete de juego
MAT_PERCENT_OVERSIZE = 1.25
MAT_HEIGHT = int(CARD_HEIGHT * MAT_PERCENT_OVERSIZE )
MAT_WIDTH = int(CARD_WIDTH * MAT_PERCENT_OVERSIZE )

#Cuanto espacio se deja entre los tapetes
#Porcentajes del tamaño del tapete
VERTICAL_MARGIN_PERCENT = 0.10
HORIZONTAL_MARGIN_PERCENT = 0.10

#Coordenada Y de fila inferior
BOTTOM_Y = MAT_HEIGHT / 2 + MAT_HEIGHT * VERTICAL_MARGIN_PERCENT

#Coordenada X donde empezaremos a poner cosas en la izqueirda
START_X = MAT_WIDTH / 2 + MAT_WIDTH * HORIZONTAL_MARGIN_PERCENT

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)



class UnoGame(arcade.Window):
    """
    CLase para juego UNO
    """
    def __init__(self, width, height, title, fullscreen=False, resizable=False, update_rate=1 /60, antialiasing=True):
        super().__init__(width=width, height=height, title=title, fullscreen=fullscreen, resizable=resizable, update_rate=update_rate, antialiasing=antialiasing)
        #Definir sprites de las cartas.
        self.lista_cartas = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()
        self.paused = False

    def setup(self):
        """
        Preparar el juego para jugar.
        """
        #Poner un color de fondo.
        arcade.set_background_color(arcade.color.SKY_BLUE)

        #Configurar Mazo

        self.deck = Mazo()
        self.deck.inicializar()

        for card in self.deck.cartas:
            carta = arcade.Sprite(card.im_filename,CARD_SCALE)
            carta.center_y = self.height / 2
            carta.left = 10
            self.all_sprites.append(carta)

    def on_key_press(self, symbol, modifiers):
        """Manejar los inputs del usuario en el teclado
        Q: Salir del Juego
        P: Pausar:
        Argumentos:
            symbol {int} -- Cual tecla fue presionada
            modifiers {int} -- Which modifiers were pressed
        """
        if symbol == arcade.key.Q:
            #Salir inmediatamente
            arcade.close_window()
        
        if symbol == arcade.key.P:
            self.paused = not self.paused

        if symbol == arcade.MOUSE_BUTTON_RIGHT:
            lol
    
    def on_update(self, delta_time: float):
        """Actualizar el frame
        Argumentos:
            delta_time {float} -- Tiempo desde la ultima actualizacion
        """
        #Si estamos pausados, no actualizamos nada
        if self.paused:
            return

        #Actualizar todo lo demas
        self.all_sprites.update()

        #Mas cosas por hacer ...

    def on_draw(self):
        """Dibuja todos los objetos del juego en pantalla
        """
        arcade.start_render()
        self.all_sprites.draw()




def Game():
    
    Juego = UnoGame(SCREEN_HEIGHT,SCREEN_WIDTH,SCREEN_TITLE)
    #ABRIR UNA VENTANA: 
    Juego.setup()

    #Mostrar todo
    arcade.run()

if __name__ == "__main__":
    Game()

