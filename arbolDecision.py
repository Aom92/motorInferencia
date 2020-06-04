from NodoPosibilidad import NodoPosibilidad

class ArbolDecision:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root
    
    def setRoot(self, carta):
        self.root = NodoPosibilidad(carta)
    
    def insertPosibilities(self, lista, mano, niveles, nodo):
        if niveles == 0:
            return
        elif nodo.getValue().getEfecto() != "":
            return

        #if(niveles%2 == 0):
        if(niveles % 2 != 0):
            for i in mano:
                carta = nodo.getValue()
                if i.getColor() == carta.getColor():
                    nodoAInsrtar = NodoPosibilidad(i)
                    nodo.insertByColor(nodoAInsrtar)
                if i.getValue() == carta.getValue():
                    nodoAInsrtar = NodoPosibilidad(i)
                    nodo.insertByNumber(nodoAInsrtar)
                #if i.getEfecto() == carta.getEfecto():
                    #nodoAInsrtar = NodoPosibilidad(i)
                    #nodo.insertByNumber(nodoAInsrtar)
        else:
            for i in lista:
                carta = nodo.getValue()
                if i.getColor() == carta.getColor():
                    nodoAInsrtar = NodoPosibilidad(i)
                    nodo.insertByColor(nodoAInsrtar)
                if i.getValue() == carta.getValue():
                    nodoAInsrtar = NodoPosibilidad(i)
                    nodo.insertByNumber(nodoAInsrtar)
                #if i.getEfecto() == carta.getEfecto():
                    #nodoAInsrtar = NodoPosibilidad(i)
                    #nodo.insertByNumber(nodoAInsrtar)

        newLista = []
        newMano = []

        for i in lista:
            newLista.append(i)

        for i in mano:
            newMano.append(i)

        #if(niveles%2 == 0):
        if(niveles%2 != 0):
            position = 0
            for i in mano:
                if i.toString() == nodo.getValue().toString():
                    break
                position = position + 1
        
            if(position < len(mano)):
                newMano.pop(position)
            #mano.pop(mano.index(nodo))
        else:
            position = 0
            for i in lista:
                if i.toString() == nodo.getValue().toString():
                    break
                position = position + 1

            if(position < len(lista)):
                lista.pop(position)
            #lista.pop(lista.index(nodo))

        for i in nodo.getColorCarts():
            #self.insertPosibilities(lista,niveles-1,i)
            self.insertPosibilities(lista,mano,niveles-1,i)

        for i in nodo.getNumberCarts():
            #self.insertPosibilities(lista,niveles-1,i)
            self.insertPosibilities(lista,mano,niveles-1, i)

    def getPosibilities(self,posibilidades,nodo, lista, profundidad):

        if(profundidad == 0):
            posibilidades.restartPosibilities()

        lista = lista + "=>" + nodo.getValue().toString()
        profundidad = profundidad+1
        
        if(len(nodo.getColorCarts())==0 and len(nodo.getNumberCarts())==0):
            posibilidades.insertValue((profundidad,lista))
            posibilidades.incrementIterator()
            return

        for i in nodo.getNumberCarts():
            self.getPosibilities(posibilidades,i,lista,profundidad+1)

        for i in nodo.getColorCarts():
            self.getPosibilities(posibilidades,i,lista,profundidad+1)
        
        

    