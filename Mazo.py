from Carta import Carta
import random
class Mazo:
    """
    Constructor de un Objeto Mazo
    """
    def __init__(self):
        self.cartas = []
        self.generar()
        
    """
    Genera un nuevo deck de UNO con 108 Cartas de 4 Colores
    """
    def generar(self):
        for Color in ["Rojo", "Azul", "Amarillo", "Verde"]:
            for Numero in range(0,10):
                self.cartas.append(Carta(Numero,Color,""))
            for Numero in range(0,10):
                self.cartas.append(Carta(Numero,Color,""))
            for Especial in ["Salto", "Reversa", "+2"]:
                self.cartas.append(Carta("",Color,Especial))
                self.cartas.append(Carta("",Color,Especial))
            for Comodin in ["Comodin","Comodin +4"]:
                self.cartas.append(Carta("","",Comodin))                
    """
    Imprime todas las cartas dentro del Mazo
    """
    def mostrar(self):
        for carta in self.cartas:
            carta.mostrar()

    """
    Revuelve el mazo utilizando el Algoritmo de Fisher-Yates 
    """
    def revolver(self):
        for i in range(len(self.cartas)-1,0,-1):
            r = random.randint(0,i)
            self.cartas[i], self.cartas[r] = self.cartas[r], self.cartas[i]

    """
    Toma una carta del mazo
    """
    def tomarCarta(self):
        if (len(self.cartas)== 0):
            print("No quedan Cartas en el mazo")
            return None
        return self.cartas.pop()
    
"""
Ejemplo de uso
deck = Mazo()
print( deck.cartas.__len__())
deck.mostrar()
print("========")
deck.revolver()
deck.mostrar()
"""