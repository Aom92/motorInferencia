from Carta import Carta

class Mazo:
    def __init__(self):
        self.cartas = []
        self.build()
    
    def build(self):
        for Color in ["Rojo", "Azul", "Amarillo", "Verde"]:
            for Numero in range(0,9):
                
                self.cartas.append(Carta(Numero,Color,) )
                