from Nodo import Nodo

class Arbol:

    """Funcion inicializadora de un objeto arbol, no requiere de parametros"""
    def __init__(self):
        self.root = None

    """Funcion encarga de retornar un objeto arbol"""
    def getRoot(self):
        return self.root

    """

    Funcion de activación de insertarNodo
    Recibe como parametros el valor a ingresar y la dirección a ingresar
    Al ser usado para pasar de infix a prefix la inserción depende de si la premisa era antecedente o consecuente

    """
    def insertar(self, val, direction):
        if(len(direction)==0):
            self.root = Nodo(val)
        else:
            self.insertarNodo(val, self.root, direction)

    """

    Funcion encargada de ingresar una premisa, u operador en su nodo correspondiente
    Recibe como parametros el valor a ingresar y la dirección a ingresar
    Al ser usado para pasar de infix a prefix la inserción depende de si la premisa era antecedente o consecuente

    """
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

    """Funcion encargada de recorrer el arbol en forma preorden y retornar el recorrido"""
    def preorden(self, nodo, prefix):
        if(nodo != None):
            prefix=prefix+nodo.val
            if nodo.leftChild != None:
                prefix=self.preorden(nodo.leftChild,prefix)
            
            if nodo.rightChild != None:
                prefix=self.preorden(nodo.rightChild,prefix)
                
            return prefix
        