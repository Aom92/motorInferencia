from Jugador import Jugador
from posibilidades import Posibilidades
from arbolDecision import ArbolDecision
from PAT import jugadaValida
import random


class IA(Jugador):

    def __init__(self, nombre,mazo, tablero):
        self.nombre = nombre
        self.mano = []                          #Mano de la computadora
        self.cartas = mazo.cartas               #Conjunto de cartas no jugadas y que no posee el CPU con el cual se verán las posibilidades
        self.mazo = mazo                        #Objeto mazo para usar posteriormente
        self.posibilidades = Posibilidades()    #Objeto manejador de posibilidades
        self.arbol = ArbolDecision()            #Objeto manejador del arbol de decisiones
        self.tablero = tablero                  #Tablero en que se juega 
        self.juegos = []                        #Manejador de posibles juegos
        self.contador = 0
    
    """Metodo encargado de tomar una carta del mazo"""
    def tomarCarta(self):
        self.mano.append(self.mazo.tomarCarta())
        #Buscamos borrar del conjunto de cartas no jugado las cartas que posee el CPU
        for i in self.mano:
            for j in self.cartas:
                if(j.toString()==i.toString()):
                    self.cartas.pop(self.cartas.index(j))

    """Getter de la mano de la CPU"""
    def getMano(self):
        return self.mano

    """Metodo encargado de recibir una carta, no del mazo"""
    def recibeCarta(self,carta):
        self.mano.append(carta)
    
    """Metodo encargado de actualizar los juegos posibles a futuro e indicar si todavia posibilidades calculadas"""
    def actualizaPosibilidades(self):
        #tam=0
        inDeck=False

        #Eliminamos la ultima carta jugada del conjunto de cartas posibles
        iter = 0
        for i in self.cartas:
            if(i.toString() == self.tablero.getUltimaCarta().toString()):
                self.cartas.pop(iter)
            iter = iter + 1

        #Checamos que la carta jugada se encuentre dentro de las posibilidades calculadas
        #De ser asi agregamos dichas posibilidades en la lista de nuevas posibilidades
        nuevoJuego=[] 
        for i in self.juegos:
            #print(i)
            if(len(i)>0):
                if(i[0].toString() == self.tablero.getUltimaCarta().toString()):
                    #print(self.tablero.getUltimaCarta().toString())
                    inDeck=True
                    nuevoJuego.append(i)

        #print("Saliendo")

        #Si si se hay posibilidades las actualizamos
        if(inDeck == True):
            self.juegos = []
            for i in nuevoJuego:
                self.juegos.append(i)
        else:
            #Sino indicamos que no hay
            #return False
            return False
            #self.actualizaPosibilidades()
            

    """Funcion encargada de dejar la siguiente carta"""
    def dejaCarta(self):        
        #Obtenemos las posibilidades (Siempre se ven n turnos a futuro)
        self.getPosibilities()
        if(len(self.juegos)==0):
            self.actualizaPosibilidades()
        if(len(self.juegos)==0):
                return False
        out = False
        cont = 0
        numeros = []
        while(out == False):
            carta = None
            if(len(self.juegos[0])<=3):
                for i in self.juegos:
                    if(len(i)>0):
                        if(i[0].getEfecto() != ""):
                            carta = i[0]
            else:
                r = random.randint(0,len(self.juegos)-1)
                if(numeros.count(r)==0):
                    numeros.append(r)
                    juego = self.juegos[r]
                    cont = cont+1
                    if(len(self.juegos)!=0):
                        carta = juego[0]
                        for i in self.mano:
                            if(i.toString() == carta.toString()):
                                out = True
            out = jugadaValida([self.tablero.getPenultimaCarta(),self.tablero.getUltimaCarta(),carta])
            #print("Jugada:",out)
            if( cont >= len(self.juegos)):
                return False

        nuevoJuego=[]
        for i in self.juegos:
            #for j in i:
                #print(j.toString(),end=",")
                #print("")
            if(i[0].toString() == carta.toString()):
                i.pop(0)
                nuevoJuego.append(i)

        self.juegos=[]
        for i in nuevoJuego:
            self.juegos.append(i)

        iter = 0
        for i in self.mano:
            if(i.toString()==carta.toString()):
                #print("Iter:",iter)
                self.mano.pop(iter)
                break
            iter = iter + 1

        #for i in self.mazo:

        return carta

    """Metodo encargado de mostrar la mano de la computadora (usado para depuracion)"""
    def mostrarMano(self):
        for carta in self.mano:
            carta.mostrar()

    """Getter del atributo Nombre"""
    def getName(self):
        return self.nombre

    """Funcion encargada de obtener todos los posibles juegos"""
    def getPosibilities(self):
        self.juegos = []
        self.arbol.setRoot(self.tablero.mano[len(self.tablero.mano)-1])
        self.arbol.insertPosibilities(self.cartas, self.mano, 5, self.arbol.getRoot())
        juegos = self.posibilidades.getCards(self.arbol)

        for i in juegos:
            if(i[len(i)-1].getEfecto() != ""):
                self.juegos.append(i)

        if(len(self.juegos)==0):
            numeros = []
            for i in range(0, int(len(juegos)/4)):
                r = random.randint(0,len(juegos)-1)
                if(numeros.count(r)==0):
                    numeros.append(r)
                    self.juegos.append(juegos[r])

        for i in self.juegos:
            if(len(i)>0):
                i.pop(0)

    """Funcion encargada de ver si es un momento optimo para dejar un comodin +4"""
    def ifDejaMasCuatro(self):
        carta = False
        color = ""
        if(self.contador < 3 or self.actualizaPosibilidades() == False):
            iter = 0
            for i in self.mano:
                if(i.getEfecto()=="Comodin +4"):
                    carta = self.mano.pop(iter)
                    colors=[0,0,0,0]
                    for i in self.mano:
                        if(i.getColor()=="Azul"):
                            colors[0] = colors[0] + 1
                        elif(i.getColor()=="Rojo"):
                            colors[1] = colors[1] + 1
                        elif(i.getColor()=="Amarillo"):
                            colors[2] = colors[2] + 1
                        else:
                            colors[3] = colors[3] + 1
                    highest = 0
                    for i in range(1,3):
                        if(colors[i]>colors[i-1]):
                            highest = highest + 1
                    opciones=["Azul","Rojo","Amarillo","Verde"]
                    color = opciones[highest]
                    return [carta,color]
                iter = iter + 1
        return [carta,color]

    """Funcion encargada de ver si es un momento optimo para dejar un comodin cambio de color"""
    def ifDejaComodinColor(self):
        carta = False
        color = ""
        if(len(self.mano)==2):
            for i in self.mano:
                if(i.getEfecto() == "Comodin"):
                    carta = i
                    if(self.mano[0].getColor()!=""):
                        color = self.mano[0].getColor()
                    else:
                        color = self.mano[1].getColor()
                    break
        elif(self.actualizaPosibilidades()==False):
            iter = 0
            for i in self.mano:
                if i.getEfecto() == "Comodin":
                    break
                iter = iter + 1
            if(iter < len(self.mano)):
                carta =self.mano.pop(iter)
                colors=[0,0,0,0]
                for i in self.mano:
                    if(i.getColor()=="Azul"):
                        colors[0] = colors[0] + 1
                    elif(i.getColor()=="Rojo"):
                        colors[1] = colors[1] + 1
                    elif(i.getColor()=="Amarillo"):
                        colors[2] = colors[2] + 1
                    else:
                        colors[3] = colors[3] + 1
                highest = 0
                for i in range(1,3):
                    if(colors[i]>colors[i-1]):
                        highest = highest + 1
                opciones=["Azul","Rojo","Amarillo","Verde"]
                color = opciones[highest]
        
        return [carta,color]
                
    """Funcion encargada de actualizar el contador de cartas del juego"""
    def setContador(self, cont):
        self.contador = cont


    

    



    


    

    
    
        


    