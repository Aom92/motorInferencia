from Carta import Carta
from Mazo import Mazo
from Jugador import Jugador
from IA import IA

import os

estado = True
update = False
turno = 0


def Draw(UNO,Tablero,IA,P1):
    #os.system("cls")

    global turno

    print("======================= U N O ! =========================")

    print("== Turno {}:  ==".format(turno))

    print("========  En la mesa... : ==========".format(Tablero.getName()))
    #print(Tablero.mano[len(Tablero.mano)-1].mostrar())
    Tablero.mostrarMano()
    print("\n")

    print("========  Cartas de {}:  ========".format(IA.getName()))
    IA.mostrarMano()
    print("\n")

    print("========  Cartas de {}:  ========".format(P1.getName()))
    P1.mostrarMano()
    print("\n")

    if(UNO):
        print("=================== CPU UNO ===================")

    print("\n")


    return 0

def IAPiensa(IA,tablero, mazo):
    if(tablero.getUltimaCarta().getEfecto=="+2"):
        IA.tomarCarta()
        IA.tomarCarta()
        return 0

    elif(tablero.getUltimaCarta().getEfecto=="Comodin +4"):
        IA.tomarCarta()
        IA.tomarCarta()
        IA.tomarCarta()
        IA.tomarCarta()
        return 0

    elif(tablero.getUltimaCarta().getEfecto=="Salto"):
        return 0

    else:
        carta = IA.ifDejaMasCuatro()
        if(carta[0]==False):

            carta = IA.ifDejaComodinColor()

            if(carta[0] == False):

                carta= IA.dejaCarta()
                while(carta==False):
                    IA.tomarCarta(mazo)
                    carta= IA.dejaCarta()
                tablero.recibeCarta(carta)
                print("Carta jugada = ",end="")
                carta.mostrar()

            else:

                print("Carta jugada = "+carta[0].mostrar())
                tablero.recibeCarta(carta[0])
                carta = Carta("",carta[1],"")
                tablero.recibeCarta(carta)
                print("Carta jugada = ",end="")
                carta.mostrar()

        else:

            print("Carta jugada = "+carta[0].mostrar())
            tablero.recibeCarta(carta[0])
            tablero.recibeCarta(Carta("",carta[1],""))
            print("Carta jugada = ",end="")
            carta.mostrar()


def juegaJugador(jugador, tablero, mazo):
    if(tablero.getUltimaCarta().getEfecto=="+2"):
        for i in range(0,2):
            jugador.tomarCarta(mazo)
        return

    elif(tablero.getUltimaCarta().getEfecto=="Comodin +4"):
        for i in range(0,4):
            jugador.tomarCarta(mazo)
        return

    elif(tablero.getUltimaCarta().getEfecto=="Salto"):
        return

    P1.mostrarMano()
    yes = input("Va a tomar carta? [Y/n]\n$ ")
    carta = None
    while(yes == "Y" or yes == "y"):
        jugador.tomarCarta(mazo)
        P1.mostrarMano()
        yes = input("Va a tomar carta? [Y/n]\n$ ")
    
    jugador.mostrarMano()
    i = int(input("ingrese carta a dejar\n$ "))
    carta = jugador.dejaCarta(i)
    print(carta.toString())
    tablero.recibeCarta(carta)

    if(carta.getEfecto()=="Comodin" or carta.getEfecto()=="Comodin +4"):
        print("Escoja el color de la siguiente carta")
        opciones = ["Azul","Rojo","Amarillo","Verde"]
        iter = 0
        for i in opciones:
            print(str(iter)+")"+ i)
            iter = iter + 1
        i = int(input("Ingrese numero correspondiente al color\n$ "))
        nuevaCarta = Carta("",opciones[i],"")
        tablero.recibeCarta(nuevaCarta)

while ( estado ):

    #Inicio del Juego
    if(turno == 0):
        #Se inicializan el mazo junto a los jugadores
        mazo = Mazo()
        P1 = Jugador("Pedrito")
        Tablero = Jugador("Tablero")
        IA = IA("PC",mazo,Tablero)

        #Se revuelve el mazo
        mazo.revolver()


        #Repartir las 7 Cartas iniciales
        for i in range(0,7):
            IA.tomarCarta()
            P1.tomarCarta(mazo)

        #Se toma una carta del Mazo para iniciar el juego:
        Tablero.tomarCarta(mazo)
        update = True
        turno = turno + 1
        if (update):
            Draw(False,Tablero,IA,P1)
            update = False


    #Logica del Juego

    #while(len(P1.getMano())>0 and len(IA.getMano())>0):
    turno = turno + 1
    juegaJugador(P1, Tablero, mazo)
    IA.setContador(len(P1.getMano()))
    IAPiensa(IA,Tablero,mazo)
    UNO=False
    if(len(IA.getMano())==1):
        UNO=True
    Draw(UNO,Tablero,IA,P1)

    


