from NodoPosibilidad import NodoPosibilidad
from arbolDecision import ArbolDecision
from Carta import Carta
from posibilidades import Posibilidades
from Mazo import Mazo

mazo = Mazo()
mazo.generar()
mazo.revolver()
mano = []

for i in range(0,7):
    mano.append(mazo.tomarCarta())

cartas = []
for i in ["Rojo", "Azul", "Amarillo", "Verde"]:
    for j in range(0,10):
        carta = Carta(j,i,"")
        cartas.append(carta)
for i in ["Rojo", "Azul", "Amarillo", "Verde"]:
    for Especial in ["Salto", "Reversa", "+2"]:
        cartas.append(Carta("",i,Especial))

for i in mano:
    for j in cartas:
        if(j.toString()==i.toString()):
            position=cartas.index(j)
            cartas.pop(position)

arbol = ArbolDecision()
arbol.setRoot(cartas[13])

arbol.insertPosibilities(cartas, mano, 5, arbol.getRoot())

posibilidades = Posibilidades()
arbol.getPosibilities(posibilidades, arbol.getRoot(), "")

for i in posibilidades.getPosibilities():
    print(i)

print(posibilidades.getNumPosibl())

print("\nMano:")
for i in mano:
    print(i.toString())

print("\nCartas:")
for i in cartas:
    print(i.toString())

