from Arbol import Arbol
from ElementGetter import getExternal
"""
    @brief Funcion que se encarga de ingresar los elementos de la expresion logica del lado izquierdo del nodo actual del arbol
    @param La expresion a revisar
    @return Una tupla con el indice en donde se encuentra el operador dentro de la expresion y el operador
"""
def  infixToPrefixLeft(expresion, direction, arbol):
    #Agregamos direccion a la izquierda
    direction.append(0)
    #Obtenemos operacion mas externa
    external=getExternal(expresion)
    #Dividimos expresion 
    if(external!=0):
        val=external[1]
        left=expresion[:external[0]]
        right=expresion[external[0]+1:]

        #Quitamos parentesis mas externos
        if(left[0]=='(' and left[len(left)-1]==')'):
            left=left[1:]
            left=left[:len(left)-1]
        if(right[0]=='(' and right[len(right)-1]==')'):
            right=right[1:]
            right=right[:len(right)-1]

        #Ingresamos operacion al arbol
        arbol.insertar(val,direction)

        #Si hay mas operaciones del lado izquierdo las separamos e ingresamos al arbol
        if(len(left)>2):
            infixToPrefixLeft(left, direction, arbol)
        else:
            #Sino ingresamos el elemento a la izquierda del nodo
            direction.append(0)
            arbol.insertar(left,direction)

        #Si hay mas operaciones del lado derecho las separamos e ingresamos al arbol
        if(len(right)>2):
            infixToPrefixRight(right, direction, arbol)
        else:
            #Sino ingresamos el elemento a la derecho del nodo
            direction.append(1)
            arbol.insertar(right,direction)


"""
    @brief Funcion que se encarga de ingresar los elementos de la expresion logica del lado derecho del nodo actual del arbol
    @param La expresion a revisar
    @return Una tupla con el indice en donde se encuentra el operador dentro de la expresion y el operador
"""
def infixToPrefixRight(expresion, direction, arbol):
    #Agregamos direccion a la derecha
    direction.append(1)
    #Obtenemos operacion mas externa
    external=getExternal(expresion)
    #Dividimos expresion 
    if(external!=0):
        val=external[1]
        left=expresion[:external[0]]
        right=expresion[external[0]+1:]

        #Quitamos parentesis mas externos
        if(left[0]=='(' and left[len(left)-1]==')'):
            left=left[1:]
            left=left[:len(left)-1]
        if(right[0]=='(' and right[len(right)-1]==')'):
            right=right[1:]
            right=right[:len(right)-1]

        #Ingresamos operacion al arbol
        arbol.insertar(val,direction)

        #Si hay mas operaciones del lado izquierdo las separamos e ingresamos al arbol
        if(len(left)>2):
            infixToPrefixLeft(left, direction, arbol)
        else:
            #Sino ingresamos el elemento a la izquierda del nodo
            direction.append(0)
            arbol.insertar(left,direction)

        #Si hay mas operaciones del lado derecho las separamos e ingresamos al arbol
        if(len(right)>2):
            infixToPrefixRight(right, direction, arbol)
        else:
            #Sino ingresamos el elemento a la derecho del nodo
            direction.append(1)
            arbol.insertar(right,direction)

def infixToPrefix(expresion):

    arbol = Arbol()

    #Obtenemos la operacion mas externa
    external=getExternal(expresion)
    #print("external:",external)
    #Si existe la operacion la separamos
    if(external!=0):
        val=external[1]
        left=expresion[:external[0]]
        right=expresion[external[0]+1:]

        #Quitamos parentesis mas externos
        if(left[0]=='(' and left[len(left)-1]==')'):
            left=left[1:]
            left=left[:len(left)-1]
        if(right[0]=='(' and right[len(right)-1]==')'):
            right=right[1:]
            right=right[:len(right)-1]

        #El arreglo direction va indicando si el elemento a ingresar va a la derecha o a la izquierda del nodo en que se encuentre
        direction=[]
        #Tras separar la expresion la ingresamos en el arbol
        arbol.insertar(val,direction)

        #Si hay mas operaciones del lado izquierdo las separamos e ingresamos al arbol
        if(len(left)>2):
            infixToPrefixLeft(left, direction, arbol)
        else:
            #La ingresamos del lado izquierdo del nodo
            direction=[0]
            arbol.insertar(left,direction)

        #Si hay mas operaciones del lado derecho las separamos e ingresamos al arbol
        if(len(right)>2):
            infixToPrefixRight(right, direction, arbol)
        else:
            #La ingresamos del derecho izquierdo del nodo
            direction=[1]
            arbol.insertar(right,direction)

        #Obtenemos la cadena correspondiente al prefix
        prefix=""
        prefix=arbol.preorden(arbol.root, prefix)
        return prefix   

    else:
        return expresion

if __name__ == "__main__":
    expresion = "(PvQ)>R"
    print(expresion)
    prefix=infixToPrefix(expresion)  
    print("Prefix:"+prefix)