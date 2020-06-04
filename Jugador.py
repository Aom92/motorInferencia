from Mazo import Mazo

class Jugador:
    """

    Constructor del jugador
    Nombre: nombre del jugador

    """
    def __init__(self, nombre):
        self.nombre = nombre
        self.mano = []
        self.topCard = None
    
    """

    Metodo encargado de que el jugador tome una carta del Mazo
    Mazo: cartas disponibles para tomar

    """
    def tomarCarta(self, mazo):
        self.mano.append(mazo.tomarCarta())

    """Getter del atributo mano"""
    def getMano(self):
        return self.mano

    """

    Metodo encargado de recibir una carta
    a diferencia de tomar carta esta no la toma del mazo
    carta: carta a recibir

    """
    def recibeCarta(self,carta):
        self.mano.append(carta)
        self.topCard = carta

    """Metodo encargado de dejar la carta indidcada por el usuario"""
    def dejaCarta(self,iterator):
        if(iterator >= len(self.mano)):
            return self.mano[len(self.mano)-1]    
        return self.mano.pop(iterator)

    """Getter de la carta indicada por el usuario"""
    def getCarta(self,iterator):
        if(iterator >= len(self.mano)):
            return self.mano[len(self.mano)-1] 
        return self.mano[iterator]

    """Metodo encargado de mostrar la mano del usuario"""
    def mostrarMano(self):
        i=0
        print(len(self.mano))
        for carta in self.mano:
            print(str(i)+") ",end="")
            carta.mostrar()
            i = i + 1
        print("\n")

    """Getter del nombre del usuario"""
    def getName(self):
        return self.nombre

    """Getter de la ultima carta en la lista del usuario"""
    def getUltimaCarta(self):
        return self.mano[len(self.mano)-1]

    """Getter de la penultima carta en la lista del usuario"""
    def getPenultimaCarta(self):
        return self.mano[len(self.mano)-2]
        


"""
Ejemplo de Uso

mazo = Mazo()
P1 = Jugador("P1")
P1.tomarCarta(mazo)
P1.mostrarMano()

"""

