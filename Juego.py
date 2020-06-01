from Carta import Carta
from Mazo import Mazo
from Jugador import Jugador

import os

estado = True
update = False
turno = 0


def Draw():

    os.system("cls")
    print("======================= U N O ! =========================")

    print("== Turno {}:  ==".format(turno))

    print("========  En la mesa... : ==========".format(Tablero.getName()))
    Tablero.mostrarMano()
    print("\n")

    print("========  Cartas de {}:  ========".format(IA.getName()))
    IA.mostrarMano()
    print("\n")

    print("========  Cartas de {}:  ========".format(P1.getName()))
    P1.mostrarMano()
    print("\n")


    print("\n")


    return 0

def IAPiensa():
    #algo:
    return 0


while ( estado ):

    #Inicio del Juego
    if(turno == 0):
        #Se inicializan el mazo junto a los jugadores
        mazo = Mazo()
        IA = Jugador("PC")
        P1 = Jugador("Pedrito")
        Tablero = Jugador("Tablero")

        #Se revuelve el mazo
        mazo.revolver()


        #Repartir las 7 Cartas iniciales
        for i in range(0,7):
            IA.tomarCarta(mazo)
            P1.tomarCarta(mazo)

        #Se toma una carta del Mazo para iniciar el juego:
        Tablero.tomarCarta(mazo)
        update = True
        turno = turno + 1
        if (update):
            Draw()
            update = False


    #Logica del Juego



    #Resto del juego
    if (update):
        Draw()
        update = False

    


