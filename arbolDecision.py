from NodoPosibilidad import NodoPosibilidad

class ArbolDecision:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root
    
    def setRoot(self, carta):
        self.root = NodoPosibilidad(carta)
    
    def insertPosibilities(self, lista, niveles, nodo):
        #print(nodo.getValue())
        if niveles == 0:
            return

        for i in lista:
            carta = nodo.getValue()
            if carta.toString() != i.toString():
                if i.getColor() == carta.getColor():
                    nodoAInsrtar = NodoPosibilidad(i)
                    nodo.insertByColor(nodoAInsrtar)
                if i.getValue() == carta.getValue():
                    nodoAInsrtar = NodoPosibilidad(i)
                    nodo.insertByNumber(nodoAInsrtar)

        newLista = []

        for i in lista:
            newLista.append(i)

        position = 0
        for i in lista:
            if i.toString() == nodo.getValue().toString():
                break
            else:
                position = position + 1
        
        if(position < len(lista)):
            newLista.pop(position)



        for i in nodo.getColorCarts():
            #self.insertPosibilities(lista,niveles-1,i)
            self.insertPosibilities(newLista,niveles-1,i)

        for i in nodo.getNumberCarts():
            #self.insertPosibilities(lista,niveles-1,i)
            self.insertPosibilities(newLista,niveles-1, i)

    def getPosibilities(self,posibilidades,nodo, lista):

        #print(posibilidades.getNumPosibl())
        #print(lista)

        lista = lista + "=>" + nodo.getValue().toString()
        
        if(len(nodo.getColorCarts())==0 and len(nodo.getNumberCarts())==0):
            posibilidades.insertValue(lista)
            posibilidades.incrementIterator()
            return

        for i in nodo.getNumberCarts():
            self.getPosibilities(posibilidades,i,lista)

        for i in nodo.getColorCarts():
            self.getPosibilities(posibilidades,i,lista)
        
        

    