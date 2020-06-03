from Carta import Carta
from arbolDecision import ArbolDecision

class Posibilidades:

    """Inicializador de objeto posibilidades, se encarga de manejar todos los posibles juegos de la IA"""
    def __init__(self):
        self.lista=[]
        self.mejores=[]
        self.cartas=[]
        self.iterator = 0
    
    """Metodo usado en caso de querer vaciar las posibilidades para volver a"""
    def restartPosibilities(self):
        self.lista = []

    """Metodo que inserta la cadena correspondiente a una posibilidad dentro de la lista de posibilidades"""
    def insertValue(self,lista):
            self.lista.append(lista)

    """Metodo que retorna el numero de jugadas posibles segun la mano de la computadora"""
    def getNumPosibl(self):
        return len(self.lista)

    """Metodo usado para incrementar el iterador de la lista"""
    def incrementIterator(self):
        self.iterator = self.iterator + 1
    
    """Getter de la lista de posibilidades"""
    def getPosibilities(self):
        return self.lista

    """

    Metodo encargado de encontrar el numero de juegos de las posibilidades mas grandes
    Requiere del arbol de decisiones para poder calcular y obtener todas las posibilidades

    """
    def getBiggestPosibility(self, arbol):
        #Calculamos de nuevo las posibilidades
        arbol.getPosibilities(self,arbol.getRoot(),"",0)
        biggest=0
        #Obtenemos el numero de juegos de la(s) mas grande(s)
        for i in self.lista:
            if(biggest < i[0]):
                biggest = i[0]
        return biggest

    """

    Metodo encargado de devolver el numero de juegos de las posibilidades mas grandes o aquellos
    que terminen con el uso de un comodin
    Requiere del arbol de decisiones para poder calcular y obtener todas las posibilidades

    """
    def getBiggestList(self,arbol):
        self.mejores = []
        #Obtenemos el valor mas grande de juego
        biggest = self.getBiggestPosibility(arbol)
        #Ingresamos a la lista de mejores juegos a todos los que tengan la longitud calculada
        for i in self.lista:
            if(i[0]==biggest):
                self.mejores.append(i)
            #Procedemos a ver si la jugada termina en comodin separando la cadena en sub cadenas
            cartas=i[1].split("=>")
            #print(i)
            mano = []

            for j in cartas:
                datos = j.split(":")
                #print(datos)
                numero = ""
                efecto = ""
                #print(datos)    
                #Obtenemos los datos de la carta para crear una nueva carta            
                if(len(datos)>1):
                    if(len(datos[0])==1):
                        numero = datos[0]
                    else:
                        efecto = datos[0]
                    color = datos[1]
                    mano.append(Carta(numero,color,efecto))
            #Si la ultima carta del juego es un comodin la agregamos a la lista
            if(mano[len(mano)-1].getEfecto()!=""):
                self.mejores.append(i)
    
    """

    Metodo encargado de pasar las cadenas de posibilidades a listas con la secuencia de cartas
    a usar por la computadora
    A su vez es metodo activador de getBiggestList, por lo cual requiere del parametro arbol

    """
    def getCards(self, arbol):
        self.getBiggestList(arbol)
        self.cartas=[]
        for i in self.mejores:
            mano=[]
            #print(i)
            #Separamos la cadena de acuerdo al signo de consecuencia
            cartas=i[1].split("=>")
            #print(i)
            for j in cartas:
                #La lista de cadenas resultantes la dividimos en donde hallan :
                #La lista resultante contiene dos partes [0] (numero o efecto) y [1] (color)
                datos = j.split(":")
                #print(datos)
                numero = ""
                efecto = ""
                #print(datos)                
                if(len(datos)>1):
                    if(len(datos[0])==1):
                        numero = datos[0]
                    else:
                        efecto = datos[0]
                    color = datos[1]
                    #Creamos la carta correspondiente a dicho paso y la agregamos dentro de una lista
                    mano.append(Carta(numero,color,efecto))
            #Ingresamos dicha posibilidad a la lista de cartas a jugar
            self.cartas.append(mano)
        return self.cartas

    """Getter de la lista de mejores posibilidades"""
    def getMejores(self):
        return self.mejores