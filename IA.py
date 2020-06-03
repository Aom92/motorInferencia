from Jugador import Jugador
from posibilidades import Posibilidades
from arbolDecision import ArbolDecision
from PAT import jugadaValida
from Carta import Carta
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
    def tomarCarta(self, mazo):
        self.mano.append(mazo.tomarCarta())
        #Buscamos borrar del conjunto de cartas no jugado las cartas que posee el CPU
        for i in self.mano:
            for j in self.cartas:
                if(j.toString()==i.toString()):
                    self.cartas.pop(self.cartas.index(j))
        self.getPosibilities()

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
        print("Falg 1")
        #Si por algun motivo no hay jugadas y tras actualizar siguen sin haber posibles retornamos que no hay carta a dejar
        if(len(self.juegos)==0):
            self.actualizaPosibilidades()
        if(len(self.juegos)==0):
                return False
        
        print("Flag 2")
        #Checamos entre las mejores jugadas y elejimos un juego al azar
        out = False
        cont = 0
        numeros = []
        carta = None

        #Si quedan pocos juegos le damos prioridad a los comodines
        if(len(self.juegos[0])<=1):
            for i in self.juegos:
                #print("Flag 3")
                if(len(i)>0):
                    if(i[0].getEfecto() != "" and (i[0].getColor()=="" or i[0].getColor() == self.tablero.getUltimaCarta().getColor())):
                        print("Flag 4")
                        carta = i[0]
                        out = True
                        break
        else:
            while(out == False):
                carta = Carta("","","")
                #Si no agarramos una de entre todas las cartas
                r = random.randint(0,len(self.juegos)-1)
                if(numeros.count(r)==0):
                    print(r)
                    numeros.append(r)
                    #Obtenemos el r-esimo juego y su primera carta
                    juego = self.juegos[r]
                    cont = cont+1
                    if(len(self.juegos)!=0):
                        carta = juego[0]
                        #Si la carta esta en la mano de la IA, que deberia, checamos si es valido usando PAT
                        for i in self.mano:
                            if(i.toString() == carta.toString()):
                                out = jugadaValida([self.tablero.getPenultimaCarta(),self.tablero.getUltimaCarta(),carta])
                                break
                print("Jugada:",out)
                #Igualmente checamos que no hayamos intentado ya con todas las posibilidades que hay
                if( cont >= len(self.juegos)):
                    return False

        print("Saliendo")

        if(type(carta) is type(None)):
            return False

        #Ya que el juego es valido obtenemos todos los juegos que contienen esa carta en dicho paso
        nuevoJuego=[]
        for i in self.juegos:
            if(len(i)>0):
                if(type(i[0]) is type(carta)):
                    if(i[0].toString() == carta.toString()):
                        i.pop(0)
                        nuevoJuego.append(i)

        #Actualizamos la lista de juegos
        self.juegos=[]
        for i in nuevoJuego:
            self.juegos.append(i)

        #Eliminamos la carta de nuestra mano
        iter = 0
        for i in self.mano:
            if(type(i) is type(carta)):
                if(i.toString()==carta.toString()):
                    self.mano.pop(iter)
                    break
            iter = iter + 1

        #La retornamos
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
        #Reiniciamos la lista de opciones
        self.juegos = []
        #Hacemos que el arbol vuelva a calcular las posibilidades y las guardamos en una lista
        self.arbol.setRoot(self.tablero.mano[len(self.tablero.mano)-1])
        self.arbol.insertPosibilities(self.cartas, self.mano, 5, self.arbol.getRoot())
        juegos = self.posibilidades.getCards(self.arbol)


        for i in juegos:
            if(i[len(i)-1].getEfecto() != ""):
                self.juegos.append(i)

        #Si las posibilidades siguen vacías obtenemos un n numero de jugadas
        #if(len(self.juegos)==0):
        numeros = []
        for i in range(0, int(len(juegos)/3)):
            r = random.randint(0,len(juegos)-1)
            if(numeros.count(r)==0):
                numeros.append(r)
                self.juegos.append(juegos[r])

        #No se que hace esta linea, favor de no quitar
        for i in self.juegos:
            if(len(i)>0):
                i.pop(0)

        #print("Juegos:",self.juegos)

    """Funcion encargada de ver si es un momento optimo para dejar un comodin +4"""
    def ifDejaMasCuatro(self):
        carta = False
        color = ""
        #Checamos que sea un momento optimo para tirarlo o que no tengamos mas cartas
        if(self.contador < 3 or self.actualizaPosibilidades() == False):
            iter = 0
            #Checamos que tengamos el comodin
            for i in self.mano:
                if(i.getEfecto()=="Comodin +4"):
                    carta = self.mano.pop(iter)
                    #Buscamos cual es el color mas presente en nuestra mano para cambiar a usar dicho color
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
                    #Vemos de que color se presentan mas
                    for i in range(1,3):
                        if(colors[i]>colors[i-1]):
                            highest = highest + 1
                    opciones=["Azul","Rojo","Amarillo","Verde"]
                    #Retornamos la carta +4 y el color a que cambiaremos
                    color = opciones[highest]
                    return [carta,color]
                iter = iter + 1
        #Retornamos que no hay carta +4 y no cambiaremos de color
        return [carta,color]

    """Funcion encargada de ver si es un momento optimo para dejar un comodin cambio de color"""
    def ifDejaComodinColor(self):
        carta = False
        color = ""
        #Checamos que sea un momento optimo para tirarlo o que no tengamos mas cartas
        if(len(self.mano)==2):
            for i in self.mano:
                #Vemos que tenemos el comodin en caso de que queden solo dos cartas
                if(i.getEfecto() == "Comodin"):
                    carta = i
                    #Checamos el color de la otra carta para cambiar a dicho color
                    if(self.mano[0].getColor()!=""):
                        color = self.mano[0].getColor()
                    else:
                        color = self.mano[1].getColor()
                    break
        elif(self.actualizaPosibilidades()==False):
            iter = 0
            #En caso de no tener cartas para tirar obtenemos la carta
            for i in self.mano:
                if i.getEfecto() == "Comodin":
                    break
                iter = iter + 1
            if(iter < len(self.mano)):
                carta =self.mano.pop(iter)
                #Proceso para ver cuantas cartas hay de cada color
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
                #Vemos que carta hay de mas colores
                highest = 0
                for i in range(1,3):
                    if(colors[i]>colors[i-1]):
                        highest = highest + 1
                opciones=["Azul","Rojo","Amarillo","Verde"]
                color = opciones[highest]
        
        #Retornamos la carta +4 y el color a que cambiaremos o que no tenemos la carta segun el caso
        return [carta,color]
                
    """Funcion encargada de actualizar el contador de cartas del juego"""
    def setContador(self, cont):
        self.contador = cont


    

    



    


    

    
    
        


    