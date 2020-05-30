from Mazo import Mazo

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mano = []
    
    def tomarCarta(self, mazo):
        self.mano.append(mazo.tomarCarta())
        return self

    def mostrarMano(self):
        for carta in self.mano:
            carta.mostrar()


"""
Ejemplo de Uso

mazo = Mazo()
P1 = Jugador("P1")
P1.tomarCarta(mazo)
P1.mostrarMano()

"""

