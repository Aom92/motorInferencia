class Carta:
    """
    Constructor de un objeto carta
    numero: Numero de la carta
    color: Color de la carta
    efecto: En este argumento se debera preferiblemente con una cadena que describa el efecto especial de alguna carta, como los comodines, toma dos, reversas y saltos.
    """
    def __init__(self, numero, color, efecto):
        self.numero = numero
        self.color = color
        self.efecto = efecto
    
    """Imprime los atributos de la carta"""
    def mostrar(self):
        if(self.efecto == ""):
             print("{} de color {}".format(self.numero,self.color))
        else: 
            if(self.color == ""):   
                print("{}".format(self.efecto))
            else:
                print("{} de color {}".format(self.efecto, self.color))

    """Getter del atributo Efecto de la carta"""
    def getEfecto(self):
        return self.efecto

    """Getter del atributo Color de la carta"""
    def getColor(self):
        return self.color

    """Getter del atributo Numerico de la carta"""
    def getValue(self):
        return self.numero

    """Metodo encargado de pasar a texto los atributos de la carta"""
    def toString(self):
        if(self.efecto!=""):
            return "{}:{}".format(self.efecto,self.color)
        return "{}:{}".format(self.numero,self.color)
    


"""
Ejemplo de uso 
Carta()
Carta = Carta(1,"Rojo","")
Carta.mostrar()    
"""