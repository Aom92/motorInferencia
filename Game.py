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
        self.paused = False

    def setup(self):
        """
        Preparar el juego para jugar.
        """
        #Poner un color de fondo.
        arcade.set_background_color(arcade.color.SKY_BLUE)

        #Configurar Mazo
        for num in range(0,108):
            carta = arcade.Sprite("images/UNO-Card_"+str(num)+".png",SCALING)
            carta.center_y = self.height / 2
            #carta.left = 10
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



Juego = UnoGame(SCREEN_HEIGHT,SCREEN_WIDTH,SCREEN_TITLE)

#ABRIR UNA VENTANA:

Juego.setup()


#Mostrar todo
arcade.run()