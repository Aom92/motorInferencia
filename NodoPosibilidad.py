class NodoPosibilidad:
    def __init__(self, carta):
        self.carta = carta
        self.listaColor = []
        self.listaNumeros = []

    def insertByColor(self,carta):
        self.listaColor.append(carta)

    def insertByNumber(self,carta):
        self.listaNumeros.append(carta)

    def getNumberCarts(self):
        return self.listaNumeros
    
    def getColorCarts(self):
        return self.listaColor

    def getValue(self):
        return self.carta

    