from infixToPrefix import infixToPrefix
from ElementGetter import getElementsPrefix, getElements
from Stack import Stack
from Carta import Carta
import copy


"""

Funcion encargada de pasar una lista de cartas a una lista de premisas legibles para el proceso del PAT
Su parametro es la lista a modificar
Retorna las listas de antecedente y consecuente legibles para el PAT

"""
def traductorColor(listaCartas):
    left = []
    #Itermanos la lista
    for i in range(0,3):
        color = ""
        numero = ""
        #Checamos color
        if(listaCartas[i].getColor()=="Azul"):
            color = "B"
        elif(listaCartas[i].getColor()=="Rojo"):
            color = "R"
        elif(listaCartas[i].getColor()=="Amarillo"):
            color = "Y"
        else:
            color = "G"

        #Si no tiene color le ponemos una E de efecto
        if(listaCartas[i].getEfecto()!=""):
            numero="E"
        else:
            #Si no tiene valor numerico ni color ponemos una C de comodin
            if(listaCartas[i].getColor()==""):
                numero="C"
            else:
                numero = ""+str(listaCartas[i].getValue())
        
        if(i<2):
            left.append(color)
        else:
            left.append("("+color+"^"+numero+")")

    #Creamos el antecedente y consecuente para probar el principio de transitividad
    toReturnRight=[] 
    toReturnRight.append(left[0]+">"+left[2])
    toReturnLeft = []
    toReturnLeft.append(left[0]+">"+left[1])
    expresion = left[2]
    toReturnLeft.append(expresion[1]+">"+expresion)

    print(toReturnLeft)
    print(toReturnRight)

    return [toReturnLeft,toReturnRight]

"""

Funcion encargada de pasar una lista de cartas a una lista de premisas legibles para el proceso del PAT
Su parametro es la lista a modificar
Retorna las listas de antecedente y consecuente legibles para el PAT

"""
def traductorNumero(listaCartas):
    left = []
    #Itermanos la lista
    for i in range(0,3):
        color = ""
        numero = ""
        #Checamos color
        if(listaCartas[i].getColor()=="Azul"):
            color = "B"
        elif(listaCartas[i].getColor()=="Rojo"):
            color = "R"
        elif(listaCartas[i].getColor()=="Amarillo"):
            color = "Y"
        else:
            color = "G"

        #Si no tiene color le ponemos una E de efecto
        if(listaCartas[i].getEfecto()!=""):
            numero="E"
        else:
            #Si no tiene valor numerico ni color ponemos una C de comodin
            if(listaCartas[i].getColor()==""):
                numero="C"
            else:
                numero = ""+str(listaCartas[i].getValue())
        
        if(numero == ""):
            numero = "N"
        
        if(i<2):
            left.append(numero)
        else:
            left.append("("+color+"^"+numero+")")

    #Creamos el antecedente y consecuente para probar el principio de transitividad
    toReturnRight=[] 
    toReturnRight.append(left[0]+">"+left[2])
    toReturnLeft = []
    toReturnLeft.append(left[0]+">"+left[1])
    expresion = left[2]
    toReturnLeft.append(expresion[3]+">"+expresion)

    print(toReturnLeft)
    print(toReturnRight)

    return [toReturnLeft,toReturnRight]
"""

    Funcion que evalua una expresion del antecedentes del metodo de Prueba automatica de teoremas
    Sus parametros son: la expresion a evaluar, el indice donde se encuentra dicha expresion 
    y la pila donde se encuentran las evaluaciones
    Retorna la pila modificada

"""
def evaluacionIzquierda(expresion, indice, stack):

    #print(expresion)
    #Checa si se esta negando una premisa logica para poder aplicar la operacion correspondiente
    if((expresion[0]=='!' and expresion[1]=='(') or (len(expresion)==2 and expresion[0]=='!')):
        cambio=stack.pop()
        cambio[0].pop(indice)
        cambio[1].append(expresion[1:])
        stack.push(cambio)
        return stack

    #Obtenemos los elementos de la expresion [lado izquierdo, operacion, lado derecho]
    elements=getElementsPrefix(expresion)
    if(elements[0]=='^'):
        #Caso de operador AND en antecedente
        cambio=stack.pop()
        cambio[0].pop(indice)
        cambio[0].append(elements[1])
        cambio[0].append(elements[2])
        stack.push(cambio)
        return stack

    elif(elements[0]=='v'):
        #Caso de operador OR en antecedente
        tupla1=stack.pop()
        tupla1[0].pop(indice)
        tupla2=copy.deepcopy(tupla1)

        stack.push(tupla1)
        cambio1=stack.pop()
        cambio1[0].append(elements[1])
        stack.push(cambio1)

        stack.push(tupla2)
        cambio2=stack.pop()
        cambio2[0].append(elements[2])
        stack.push(cambio2)
        return stack

    elif(elements[0]=='>'):
        #Caso de operador IF en antecedente
        tupla1=stack.pop()
        tupla1[0].pop(indice)
        tupla2=copy.deepcopy(tupla1)

        stack.push(tupla1)
        cambio1=stack.pop()
        cambio1[0].append(elements[2])
        stack.push(cambio1)

        stack.push(tupla2)
        cambio2=stack.pop()
        cambio2[1].append(elements[1])
        stack.push(cambio2)
        return stack

"""
    Funcion que evalua una expresion del consecuente del metodo de Prueba automatica de teoremas
    Sus parametros son: la expresion a evaluar, el indice donde se encuentra dicha expresion
    y la pila donde se encuentran las evaluaciones
    Retorna la pila modificada 
"""
def evaluacionDerecha(expresion, indice, stack):
    #print(expresion)

    #Checa si se esta negando una premisa logica para poder aplicar la operacion correspondiente
    if((expresion[0]=='!' and expresion[1]=='(')  or (len(expresion)==2 and expresion[0]=='!')):
        cambio=stack.pop()
        cambio[1].pop(indice)
        cambio[0].append(expresion[1:])
        stack.push(cambio)
        return stack

    #Obtenemos los elementos de la expresion [operacion, lado izquierdo, lado derecho]
    elements=getElementsPrefix(expresion)
    #Caso de encontrar un operador and en consecuente
    if(elements[0]=='^'):
        tupla1=stack.pop()
        tupla1[1].pop(indice)
        tupla2=copy.deepcopy(tupla1)

        stack.push(tupla1)
        cambio1=stack.pop()
        cambio1[1].append(elements[2]) 

        stack.push(cambio1)

        stack.push(tupla2)
        cambio2=stack.pop()
        cambio2[1].append(elements[1])
        stack.push(cambio2)
        return stack

    elif(elements[0]=='v'):
        #Caso de encontrar un operador or en consecuente
        cambio=stack.pop()
        cambio[1].pop(indice)
        cambio[1].append(elements[1])
        cambio[1].append(elements[2])
        stack.push(cambio)
        return stack

    elif(elements[0]=='>'):
        #Caso de encontrar un operador if en consecuente
        cambio=stack.pop()
        cambio[1].pop(indice)
        cambio[0].append(elements[1])
        cambio[1].append(elements[2])
        stack.push(cambio)
        return stack

"""

    Funcion que se encarga de ir enviando las distintas expresiones a sus respectivas evaluaciones hasta que todas sean atomicas
    Sus parametros son: la pila que contiene el proceso de evaluacion
    Retorna el valor retornado al checar si es valido

"""
def evaluarExpresion(stack):
    expresionesFinales=[]
    finished=False

    while(finished != True):
        tupla=stack.peek()
        left=tupla[0]
        indexLeft=0
        #Iteramos los elementos del antecedente hasta encontrar uno que no sea atomico
        for i in left:
            if(len(i)==1):
                #Si es atomico aumentamos el inidice para indicar en que posicion se encuentra la no atomica
                indexLeft=indexLeft+1
            else:
                #Si no es atomica la mandamos a evaluar
                evaluacionIzquierda(i,indexLeft,stack)
                break

        tupla=stack.peek()
        right=tupla[1]
        indexRight=0
        #Iteramos los elementos del consecuente hasta encontrar uno que no sea atomico
        for i in right:
            if(len(i)==1):
                #Si es atomico aumentamos el inidice para indicar en que posicion se encuentra la no atomica
                indexRight=indexRight+1
            else:
                #Si no es atomica la mandamos a evaluar
                evaluacionDerecha(i,indexRight,stack)
                break

        #Si recorremos tanto antecedente como consecuente y unicamente encontramos atomicas lo ingresamos en el arreglo de expresiones finales
        if(indexLeft==len(left) and indexRight==len(right)):
            expresionesFinales.append(stack.pop())
            if(stack.top()==0):
                finished=True

    return checarSiValido(expresionesFinales)

"""

    Funcion que checa si todas las premisas resultantes son acciomas
    Sus parametros son una lista con todas las expresiones resultantes de la evaluacion
    Retorna un valor booleano indicando si es o no valida la expresion

"""
def checarSiValido(expresiones):
    #print(len(expresiones))
    axiomas=[]
    #Iteramos las expresiones finales
    for i in expresiones:
        #print(i)
        left=i[0]
        right=i[1]
        trueLeft=True
        trueRight=True

        #Arreglo que se encarga de guardar las expresiones atomicas del lado 
        #izquierdo para su posterior comparación con el lado derecho
        atomicLeft=[]

        #Checamos que todos los elementos en el antecedente sean atomicas
        for j in left:
            #Si no es atomica indicamos que el lado izquierdo no corresponde a axiomas
            if len(j)>1:
                trueLeft=False
                break
            else:
                atomicLeft.append(j)
        
        #checamos que todos los elementos en el consecuente sean premisas 
        inLeft=[]
        for k in right:
            #Si no es atomica indicamos que el lado derecho no corresponde a axiomas
            if len(k)>1:
                trueRight=False
                break
            else:
                #Checamos si los elementos de la derecha se encuentran en la izquierda
                for ij in atomicLeft:
                    if ij == k:
                        inLeft.append(True)
                        break
                    else:
                        inLeft.append(False)

        #Si no hay elementos del antecedente en el consecuente indicamos que es erroneo
        if(inLeft.count(True)<=0):
            trueRight=False

        #Si el lado del antecedente y consecuente son correctos entonces la expresion final es un axioma
        if(trueLeft and trueRight):
            axiomas.append(True)
        else:
            axiomas.append(False)

    #Si todas son aciomas indicamos que las premisas y conclusion son validas
    if((len(axiomas) == len(expresiones)) and (axiomas.count(False)<=0)):
        return True
    else:
        return False

"""

Funcion activadora del resto de las funciones del archivo
Metodo encargado de checar si la jugada recibida es valida
Retorna si la jugada es valida

"""
def jugadaValida(listaCartas):

    #Hacemos dos chequeos: chequeo de validez por color y chequeo por número

    infixToPrefixArrayLeft=[]
    infixToPrefixArrayRight=[]
    #Traducimos la lista de cartas a cadenas, enfocandonos en el color de las cartas, y las pasamos de infix a prefix
    listaColor = traductorColor(listaCartas)
    for x in listaColor[0]:
        infixToPrefixArrayLeft.append(infixToPrefix(x))
    for x in listaColor[1]:
        infixToPrefixArrayRight.append(infixToPrefix(x))
    stackColor = Stack()
    #Operamos dichas cadenas para ver si son validas
    stackColor.push([infixToPrefixArrayLeft,infixToPrefixArrayRight])
    validoColor = evaluarExpresion(stackColor)
    del stackColor

    infixToPrefixArrayLeft=[]
    infixToPrefixArrayRight=[]
    #Traducimos la lista de cartas a cadenas, enfocandonos en el numero de las cartas, y las pasamos de infix a prefix
    listaNumero = traductorNumero(listaCartas)
    for x in listaNumero[0]:
        infixToPrefixArrayLeft.append(infixToPrefix(x))
    for x in listaNumero[1]:
        infixToPrefixArrayRight.append(infixToPrefix(x))
    stackNumero = Stack()
    #Operamos dichas cadenas para ver si son validas
    stackNumero.push([infixToPrefixArrayLeft,infixToPrefixArrayRight])
    validoNumero = evaluarExpresion(stackNumero)
    del stackNumero

    #print("Color",validoColor)
    #print("Numero",validoNumero)
    #print("\n\n")

    #En caso de que el proceso de transitividad sea valido, ya sea por el color de las cartas o el valor numerico
    #Contamos el juego como valido
    if(validoColor == True or validoNumero == True):
        return True
    else:
        return False


if __name__ == "__main__":
    stack = Stack()

    #Posibles expresiones prueba
    left = ["((PvQ)>(!P^Q))^(P>Q)"]
    right = ["!P"]
    #left=["!A>B","B>!C","Av!D","CvD"]
    #right=["A"]
    #left = ["(PvQ)>R","!P>S","!Q>U","!R","V>(!U^!S)"]
    #right = ["!V"]

    infixToPrefixArrayLeft = []
    infixToPrefixArrayRight = []
    evaluaciones = []

    print(left,end='')
    print("=>",end='')
    print(right)
    print()

    for x in left:
        infixToPrefixArrayLeft.append(infixToPrefix(x))

    for x in right:
        infixToPrefixArrayRight.append(infixToPrefix(x))

    stack.push([infixToPrefixArrayLeft,infixToPrefixArrayRight])

    print('\nSu expresion logica '+evaluarExpresion(stack))



        




