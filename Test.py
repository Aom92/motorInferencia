from NodoPosibilidad import NodoPosibilidad
from arbolDecision import ArbolDecision
from Carta import Carta
from posibilidades import Posibilidades

cartas = []
for i in ["Rojo", "Azul", "Amarillo", "Verde"]:
    for j in range(0,10):
        carta = Carta(i,j,"")
        cartas.append(carta)

#for i in cartas:
    #print(i.toString())

arbol = ArbolDecision()
arbol.setRoot(cartas[13])

print(arbol.getRoot().getValue())

arbol.insertPosibilities(cartas,4, arbol.getRoot())

posibilidades = Posibilidades()
arbol.getPosibilities(posibilidades, arbol.getRoot(), "")

for i in posibilidades.getPosibilities():
    print(i)

print(posibilidades.getNumPosibl())

