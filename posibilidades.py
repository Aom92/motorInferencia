from Carta import Carta
from arbolDecision import ArbolDecision

class Posibilidades:
    def __init__(self):
        self.lista=[]
        self.mejores=[]
        self.cartas=[]
        self.iterator = 0
    
    def restartPosibilities(self):
        self.lista = []

    def insertValue(self,lista):
            self.lista.append(lista)

    def getNumPosibl(self):
        return len(self.lista)

    def incrementIterator(self):
        self.iterator = self.iterator + 1
    
    def getPosibilities(self):
        return self.lista

    def getBiggestPosibility(self, arbol):
        arbol.getPosibilities(self,arbol.getRoot(),"",0)
        biggest=0
        for i in self.lista:
            if(biggest < i[0]):
                biggest = i[0]
        print("Biggest {}".format(biggest))
        return biggest

    def getBiggestList(self,arbol):
        self.mejores = []
        biggest = self.getBiggestPosibility(arbol)
        for i in self.lista:
            if(i[0]==biggest):
                self.mejores.append(i)
    
    def getCards(self, arbol):
        self.getBiggestList(arbol)
        self.cartas=[]
        for i in self.mejores:
            mano=[]
            cartas=i[1].split("=>")
            print(i)
            for j in cartas:
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
                    mano.append(Carta(numero,color,efecto))
            self.cartas.append(mano)
        return self.cartas

    def getMejores(self):
        return self.mejores