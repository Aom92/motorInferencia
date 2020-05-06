from infixToPrefix import infixToPrefix
from ElementGetter import getElementsPrefix, getElements
from Stack import Stack
import copy

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
        cambio=stack.pop()
        cambio[0].pop(indice)
        cambio[0].append(elements[1])
        cambio[0].append(elements[2])
        stack.push(cambio)
        return stack

    elif(elements[0]=='v'):
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
    #@brief Funcion que evalua una expresion del consecuente del metodo de Prueba automatica de teoremas
    #@param La expresion a evaluar, el indice donde se encuentra dicha expresion y la pila donde se encuentran las evaluaciones
    #@return Checar si si es necesario
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

    #Obtenemos los elementos de la expresion [lado izquierdo, operacion, lado derecho]
    elements=getElementsPrefix(expresion)
    if(elements[0]=='^'):
        tupla1=stack.pop()
        tupla1[1].pop(indice)
        tupla2=copy.deepcopy(tupla1)

        stack.push(tupla1)
        cambio1=stack.pop()
        cambio1[1].append(elements[2]) #element[0] checar

        stack.push(cambio1)

        stack.push(tupla2)
        cambio2=stack.pop()
        cambio2[1].append(elements[1])
        stack.push(cambio2)
        return stack

    elif(elements[0]=='v'):
        cambio=stack.pop()
        cambio[1].pop(indice)
        cambio[1].append(elements[1])
        cambio[1].append(elements[2])
        stack.push(cambio)
        return stack

    elif(elements[0]=='>'):
        cambio=stack.pop()
        cambio[1].pop(indice)
        cambio[0].append(elements[1])
        cambio[1].append(elements[2])
        stack.push(cambio)
        return stack

"""

    #@brief Funcion que se encarga de ir enviando las distintas expresiones a sus respectivas evaluaciones hasta que todas sean atomicas
    #@param La pila que contiene el proceso de evaluacion
    #@return El valor retornado al checar si es valido
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
    @brief Funcion que checa si todas las premisas resultantes son acciomas
    @param Una lista con todas las expresiones resultantes de la evaluacion
    @return Por el momento una cadena diciendo si es valido o no la operacion logica
"""
def checarSiValido(expresiones):
    #print(len(expresiones))
    axiomas=[]
    #Iteramos las expresiones finales
    for i in expresiones:
        print(i)
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
        return 'es valida'
    else:
        return 'es invalida'


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



        




