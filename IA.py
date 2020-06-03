from Jugador import Jugador
from posibilidades import Posibilidades
from arbolDecision import ArbolDecision
from PAT import jugadaValida
import random


class IA(Jugador):

    def __init__(self, nombre,mazo, tablero):
        self.nombre = nombre
        self.mano = []
        self.cartas = mazo.cartas
        self.mazo = mazo
        self.posibilidades = Posibilidades()
        self.arbol = ArbolDecision()
        self.tablero = tablero
        self.juegos = []
        self.contador = 0
    
    def tomarCarta(self):
        self.mano.append(self.mazo.tomarCarta())
        for i in self.mano:
            for j in self.cartas:
                if(j.toString()==i.toString()):
                    self.cartas.pop(self.cartas.index(j))

    def getMano(self):
        return self.mano

    def recibeCarta(self,carta):
        self.mano.append(carta)
    
    def actualizaPosibilidades(self):
        #tam=0
        inDeck=False

        iter = 0
        for i in self.cartas:
            if(i.toString() == self.tablero.getUltimaCarta().toString()):
                self.cartas.pop(iter)
            iter = iter + 1

        nuevoJuego=[] 
        for i in self.juegos:
            #print(i)
            if(len(i)>0):
                if(i[0].toString() == self.tablero.getUltimaCarta().toString()):
                    #print(self.tablero.getUltimaCarta().toString())
                    inDeck=True
                    nuevoJuego.append(i)

        #print("Saliendo")

        if(inDeck == True):
            self.juegos = []
            for i in nuevoJuego:
                self.juegos.append(i)
        else:
            #return False
            return False
            #self.actualizaPosibilidades()
            


    def dejaCarta(self):        
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

    def mostrarMano(self):
        for carta in self.mano:
            carta.mostrar()

    def getName(self):
        return self.nombre

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

    def ifDejaMasCuatro(self):
        carta = False
        color = ""
        if(self.contador <= 3 or self.actualizaPosibilidades() == False):
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
                

    def setContador(self, cont):
        self.contador = cont


    

    



    


    

    
    
        


    