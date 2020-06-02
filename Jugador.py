from Mazo import Mazo

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mano = []
        self.topCard = None
    
    def tomarCarta(self, mazo):
        self.mano.append(mazo.tomarCarta())

    def getMano(self):
        return self.mano

    def recibeCarta(self,carta):
        self.mano.append(carta)
        self.topCard = carta

    def dejaCarta(self,iterator):
        return self.mano.pop(iterator)

    def mostrarMano(self):
        i=0
        print(len(self.mano))
        for carta in self.mano:
            print(str(i)+") ",end="")
            carta.mostrar()
            i = i + 1
        print("\n")

    def getName(self):
        return self.nombre

    def getUltimaCarta(self):
        return self.mano[len(self.mano)-1]
        


"""
Ejemplo de Uso

mazo = Mazo()
P1 = Jugador("P1")
P1.tomarCarta(mazo)
P1.mostrarMano()

"""

