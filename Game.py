#Testeo del modulo arcade

import arcade
import os
from Mazo import Mazo
from Jugador import Jugador


#Constantes de dibuji
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_TITLE = "TEST"

#Constantes para las cartas
CARD_SCALE = 0.6

#Que tan grande son las cartas
CARD_WIDTH = 140 * CARD_SCALE
CARD_HEIGHT = 140 * CARD_SCALE

#Que tan grande es el tapete de juego
MAT_PERCENT_OVERSIZE = 1.55
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

#Constantes que representan el proposito de cada pila en el juego.
PILE_COUNT = 4
BOTTOM_FACE_DOWN_PILE = 0
PLAYER_PILE = 1
IA_PILE = 2
PLAY_PILE = 3

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)


#PLAYER CONTANTS
JUGADOR1 = 0
IA = 0


class UnoGame(arcade.Window):
    """
    CLase para juego UNO
    """
    def __init__(self, width, height, title, fullscreen=False, resizable=False, update_rate=1 /60, antialiasing=True):
        super().__init__(width=width, height=height, title=title, fullscreen=fullscreen, resizable=resizable, update_rate=update_rate, antialiasing=antialiasing)
        
        #Entidades de juego
        self.tablero = None
        self.players = []
        
        
        #Definir sprites de las cartas.
        self.lista_cartas = arcade.SpriteList()
        
        #Lista de cartas que se esten jugando o no
        arcade.set_background_color(arcade.color.AMAZON)

        #Lista de carta que vamos a mover
        self.held_cards = None

        #Posicion original de las cartas que se estan moviendo.
        self.held_card_original_position = None

        #Sprite list con los tapetes donde se ponen las cartas 
        self.pile_mat_list = None

        #
        self.piles = []

        self.paused = False

    def setup(self):
        """
        Preparar el juego para jugar.
        """
        
        #Lista de Cartas que arrastramos con el mouse
        self.held_cards = []

        self.piles = []

        #Pilas de juego
        
        for i in range(PILE_COUNT):
            self.piles.append(arcade.SpriteList())
        

        #Posicion original de las cartas que se estan moviendo..
        self.held_card_original_position = []

        #Sprite list de las cartas
        self.lista_cartas = arcade.SpriteList()
        
        #Configurar Mazo y Jugadores

        self.deck = Mazo()
        self.deck.inicializar()
        self.deck.revolver()
        
        self.tablero = []

        self.players.append(Jugador("Player 1"))
        self.players.append(Jugador("IA"))
        
        self.players[JUGADOR1].mano = self.piles[PLAYER_PILE]
        self.players[IA].mano = self.piles[IA_PILE]

        for card in self.deck.cartas:
            carta = arcade.Sprite(card.im_filename,CARD_SCALE)
            carta.center_y = self.height / 2
            carta.position = START_X, BOTTOM_Y
            self.lista_cartas.append(carta)
        for i in range(0,7):
                
            carta = self.lista_cartas.pop()
            carta.position = START_X, BOTTOM_Y + 150
            self.piles[PLAYER_PILE].append(carta)
            carta = self.lista_cartas.pop()
            carta.position = START_X, BOTTOM_Y + 350
            self.piles[IA_PILE].append(carta)


        # --- Crear los tapetes donde las cartas van.
        # Sprite list con los tapetes donde van las cartas            
        self.pile_mat_list: arcade.SpriteList = arcade.SpriteList()

        #Crear los tapetes para las cartas boca arriba y boca abajo.
        pila = arcade.SpriteSolidColor(MAT_WIDTH,MAT_HEIGHT,arcade.csscolor.DARK_OLIVE_GREEN)
        pila.position = START_X, BOTTOM_Y
        self.pile_mat_list.append(pila)

        pila = arcade.SpriteSolidColor(MAT_WIDTH,MAT_HEIGHT,arcade.csscolor.DARK_OLIVE_GREEN)
        pila.position = START_X + X_SPACING, BOTTOM_Y
        self.pile_mat_list.append(pila)

        pila_c = arcade.SpriteSolidColor(MAT_WIDTH,MAT_HEIGHT,arcade.csscolor.DARK_OLIVE_GREEN)
        pila_c.position = SCREEN_WIDTH/2  ,SCREEN_HEIGHT/2 
        self.pile_mat_list.append(pila_c)


        
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
        self.piles[PLAYER_PILE].update()
        self.piles[IA_PILE].update()

        #Mas cosas por hacer ...

    def on_draw(self):
        """Dibuja todos los objetos del juego en pantalla
        """

        #Limpiar la pantalla
        arcade.start_render()
        #Dibujar los tapetes de cartas
        self.pile_mat_list.draw()
        #Dibujar las cartas
        self.lista_cartas.draw()
        self.piles[PLAYER_PILE].draw()
        self.piles[IA_PILE].draw()
        self.piles[PLAY_PILE].draw()

    def pull_to_top(self,card, cardpile):
        """ Pull card to top of rendering order (last to render, looks on-top) """
        # Find the index of the card
        index = cardpile.index(card)
        # Loop and pull all the other cards down towards the zero end
        for i in range(index, len(cardpile) - 1):
            cardpile[i] = cardpile[i + 1]
        # Put this card at the right-side/top/size of list
        cardpile[len(cardpile) - 1] = card            

    def on_mouse_press(self, x, y, button, modifiers):
        """Se llama cuando el usuario presiana un boton del mouse
        """
        #Revisar si hemos hecho click en la el mazo de cartas.
        cartas = arcade.get_sprites_at_point( (x,y) , self.lista_cartas)

        #Revisamos si hemos hecho click en el mazo del jugador
        if (not cartas):
            cartas = arcade.get_sprites_at_point( (x,y), self.piles[PLAYER_PILE])
            cardpile = self.piles[PLAYER_PILE]
            #Actualizar como se muestran las cartas al jugador:
            i = 0
            for carta in self.piles[PLAYER_PILE]:
                carta.position = START_X + i*25, BOTTOM_Y + 150
                i += 1
        else:
            cardpile = self.lista_cartas

        #Revisamos si hemos clickeado una carta
        if ( len(cartas) > 0 ):
            #Puede que sea una carta en una pila de cartas
            carta_primaria = cartas[-1]
            #En todos los demas casos tomaremos la carta boca arriba
            self.held_cards = [carta_primaria]
            #Guardar la posicion
            self.held_card_original_position = [self.held_cards[0].position]
            #Poner la carta en la cima
            card = self.held_cards[0]
            
            self.pull_to_top( card, cardpile )
            

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

        #Encontrar la pila de cartas mas cercana, en caso de que estemos en contacto con mas de una.
        pila, distancia = arcade.get_closest_sprite(self.held_cards[0],self.pile_mat_list)
        reiniciar_pos = True

        lcx, lcy = self.lista_cartas._get_center()
        #pcx, pcy = self.piles[PLAY_PILE]._get_center()
        if(pila.center_y == lcy):
            cardpile = self.lista_cartas
        else:
            cardpile = self.piles[PLAY_PILE]


        #Checamos si estamos en contacto con la pila mas cercana
        if arcade.check_for_collision(self.held_cards[0],pila):
            
            #Por carta, moverla en la pila que soltemos
            for i, carta_soltada in enumerate(self.held_cards):
                #Mover las cartas a la posicion adecuada.
                carta_soltada.position = pila.center_x, pila.center_y
                try:
                    cardpile.append(carta_soltada)
                    self.lista_cartas.pop(self.lista_cartas.index(carta_soltada))
                    pass
                except:
                    cardpile.append(carta_soltada)
                    self.piles[PLAYER_PILE].pop(self.piles[PLAYER_PILE].index(carta_soltada))
                    pass

            #Exito no hay que reiniciar la posicion de la carta
            reiniciar_pos = False
        
        if reiniciar_pos:
            #Donde soltamos no fue una posicion valida por lo tante regresamos al lugar inicial
            for pile_index, carta in enumerate(self.held_cards):
                carta.position = self.held_card_original_position[pile_index]
            
        





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

