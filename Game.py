#Testeo del modulo arcade

import arcade
import os
from Mazo import Mazo

#Constantes de dibuji
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_TITLE = "TEST"
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

#Constantes para los tapetes
TOP_Y = SCREEN_HEIGHT - MAT_HEIGHT / 2 - MAT_HEIGHT

MIDDLE_Y = TOP_Y - MAT_HEIGHT - MAT_HEIGHT * VERTICAL_MARGIN_PERCENT

X_SPACING = MAT_WIDTH + MAT_WIDTH * HORIZONTAL_MARGIN_PERCENT



file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)



class UnoGame(arcade.Window):
    """
    CLase para juego UNO
    """
    def __init__(self, width, height, title, fullscreen=False, resizable=False, update_rate=1 /60, antialiasing=True):
        super().__init__(width=width, height=height, title=title, fullscreen=fullscreen, resizable=resizable, update_rate=update_rate, antialiasing=antialiasing)
        #Definir sprites de las cartas.
        self.lista_cartas = None
        
        #Lista de cartas que se esten jugando o no
        arcade.set_background_color(arcade.color.AMAZON)

        #Lista de carta que vamos a mover
        self.held_cards = None

        #Posicion original de las cartas que se estan moviendo.
        self.held_card_original_position = None

        #Sprite list con los tapetes donde se ponen las cartas 
        self.pile_mat_list = None

        self.all_sprites = arcade.SpriteList()
        self.paused = False

    def setup(self):
        """
        Preparar el juego para jugar.
        """
        
        #Lista de Cartas que arrastramos con el mouse
        self.held_cards = []

        #Posicion original de las cartas que se estan moviendo..
        self.held_card_original_position = []

        #Sprite list de las cartas
        self.lista_cartas = arcade.SpriteList()
        
        #Configurar Mazo

        self.deck = Mazo()
        self.deck.inicializar()
        self.deck.revolver()

        for card in self.deck.cartas:
            carta = arcade.Sprite(card.im_filename,CARD_SCALE)
            carta.center_y = self.height / 2
            carta.position = START_X, BOTTOM_Y
            self.lista_cartas.append(carta)

        # --- Crear los tapetes donde las cartas van.
        # Sprite list con los tapetes donde van las cartas            

    def on_update(self, delta_time: float):
        """Actualizar el frame
        Argumentos:
            delta_time {float} -- Tiempo desde la ultima actualizacion
        """
        #Si estamos pausados, no actualizamos nada
        if self.paused:
            return

        #Actualizar todo lo demas
        self.lista_cartas.update()
        self.all_sprites.update()

        #Mas cosas por hacer ...

    def on_draw(self):
        """Dibuja todos los objetos del juego en pantalla
        """
        arcade.start_render()
        self.lista_cartas.draw()
        #self.all_sprites.draw()

    def pull_to_top(self,card):
        """ Pull card to top of rendering order (last to render, looks on-top) """
        # Find the index of the card
        index = self.lista_cartas.index(card)
        # Loop and pull all the other cards down towards the zero end
        for i in range(index, len(self.card_list) - 1):
            self.lista_cartas[i] = self.lista_cartas[i + 1]
        # Put this card at the right-side/top/size of list
        self.lista_cartas[len(self.lista_cartas) - 1] = card            

    def on_mouse_press(self, x, y, button, modifiers):
        """Se llama cuando el usuario presiana un boton del mouse
        """
        #Obtener la lista de cartas a la que les hemos hecho click
        cartas = arcade.get_sprites_at_point( (x,y) , self.lista_cartas)

        #Revisamos si hemos clickeado una carta.
        if ( len(cartas) > 0 ):
            #Puede que sea una carta en una pila de cartas
            carta_primaria = cartas[-1]
            #En todos los demas casos tomaremos la carta boca arriba
            self.held_cards = [carta_primaria]
            #Guardar la posicion
            self.held_card_original_position = [self.held_cards[0].position]
            #Poner la carta en la cima
            card = self.held_cards[0]
            self.pull_to_top( card )

        #return super().on_mouse_press(x, y, button, modifiers)

    def on_mouse_motion(self, x, y, dx, dy):
        """Usuario mueve el mouse
        """
        #Si estamos haciendo click en una carta esta se movera con el mouse
        for carta in self.held_cards:
            carta.center_x += dx
            carta.center_y += dy

        #return super().on_mouse_motion(x, y, dx, dy)

    def on_mouse_release(self, x, y, button, modifiers):
        """Llamada cuando el usuario deja de hacer click en un boton
        """
        #Si no tenemos cartas no ocurre nada
        if len(self.held_cards) == 0:
            return

        #Ya no estamos sosteniendo ninguna carta
        self.held_cards = []


        #return super().on_mouse_release(x, y, button, modifiers)


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

    
    




def Game():
    
    Juego = UnoGame(SCREEN_HEIGHT,SCREEN_WIDTH,SCREEN_TITLE)
    #ABRIR UNA VENTANA: 
    Juego.setup()

    #Mostrar todo
    arcade.run()

if __name__ == "__main__":
    Game()

