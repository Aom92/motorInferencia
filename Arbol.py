from Nodo import Nodo

class Arbol:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def insertar(self, val, direction):
        if(len(direction)==0):
            self.root = Nodo(val)
        else:
            self.insertarNodo(val, self.root, direction)

    def insertarNodo(self, val, nodo, direction):
        #Dependiendo de la direccion indicada por el programa activacion es en que hijo se ingresara el valor enviado
        if(direction[0]==0):
            if(nodo.leftChild == None):
                nodo.leftChild = Nodo(val)
            else:
                self.insertarNodo(val, nodo.leftChild, direction[1:])
        else:
            if(nodo.rightChild == None):
                nodo.rightChild = Nodo(val)
            else:
                self.insertarNodo(val, nodo.rightChild, direction[1:])

    def preorden(self, nodo, prefix):
        if(nodo != None):
            prefix=prefix+nodo.val
            if nodo.leftChild != None:
                prefix=self.preorden(nodo.leftChild,prefix)
            
            if nodo.rightChild != None:
                prefix=self.preorden(nodo.rightChild,prefix)
                
            return prefix
        