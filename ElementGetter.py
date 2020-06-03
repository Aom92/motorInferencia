def my_range(start, end, step):
    while start>=end:
        yield start
        start += step

"""
    Funcion que se encarga de encontrar la operacion mas externa dentro de una expresion logica
    Paramretro recibido: la expresion a revisar
    Retorna una tupla con el indice en donde se encuentra el operador dentro de la expresion y el operador
"""
def getExternal(expresion):
    numParentesis=0
    #Iteramos la expresion
    for i in range (0, len(expresion)):
        #Si es un parentesis de apertura lo indicamos aumentando numParentesis (me dio flojera usar pilas) y si es de cierre lo disminuimos
        if(expresion[i] == '('):
            numParentesis=numParentesis+1
        elif(expresion[i] == ')'):
            numParentesis=numParentesis-1
        elif(expresion[i]=='v' or expresion[i]=='^' or expresion[i]=='>'):
            #Checamos que no se encuentre dentro de una serie de parentesis
            if(numParentesis == 0):
                toReturn=(i,expresion[i])
                return toReturn
    else:
        return 0


"""
    Funcion que se encarga de dividir la expresion logica en [antes de operador, operador, despues de operador]
    Paramtero: la expresion a revisar
    Retorna lista con los elementos de la operacion en caso de haber una o 0 en caso de no haberlo
"""
def getElements(expresion):
    #Buscamos el operador mas externo
    external=getExternal(expresion)

    #Si hay un operador externo continuamos
    if(external!=0):
        val=external[1]
        left=expresion[:external[0]]
        right=expresion[external[0]+1:]

        #Extraemos los parentesis
        if(left[0]=='(' and left[len(left)-1]==')'):
            left=left[1:]
            left=left[:len(left)-1]
        if(right[0]=='(' and right[len(right)-1]==')'):
            right=right[1:]
            right=right[:len(right)-1]

        #Retornamos la lista con antecedente, operador, consecuente
        lista = [left,external[1],right]
        return lista
    return 0

def getElementsPrefix(expresion):
    #Iteramos de final a inicio
    iterator = len(expresion)-1
    operator=''
    operandA=''
    operandB=''
    operation=[]
    #Revisamos que la expresion no sea unicamente una negacion y un caracter
    if(len(expresion)<=2):
        return [expresion]
    
    i = 0

    #Buscamos el operador mas externo
    if(expresion[i]=='^' or expresion[i]=='v' or expresion[i]=='>'):
        operator+=expresion[i]
        #Checamos si despues de dicho operador hay uno
        if(expresion[i+1]=='^' or expresion[i+1]=='v' or expresion[i+1]=='>'):
            #Checamos si despues de dicho operador hay otro
            if(expresion[i+2]=='^' or expresion[i+2]=='v' or expresion[i+2]=='>'):
                operandA=expresion[i+1]+expresion[i+2]

                acum = 0
                desplazamiento = 0
                #Creamos la expresion en caso de que hayan operadores en antecedente y consecuente
                for j in range(i+3,len(expresion)):
                    if(expresion[j]=='^' or expresion[j]=='v' or expresion[j]=='>'):
                        acum = acum + 1
                    if(acum == 2):
                        break
                    desplazamiento = desplazamiento + 1
                operandA = expresion[i+1:]
                operandA = operandA[:desplazamiento+2]
                operandB = expresion[desplazamiento+3:]

            else:
                
                #Checamos los elementos de los que pueden estar compuestos el antecedente (dos premisas y posibles dos negaciones)
                #El consecuente es todo lo que le sigue
                operandA+=expresion[i+1]
                if(expresion[i+2]=='!'):
                    operandA+=expresion[i+2]+expresion[i+3]
                    if(expresion[i+4]=='!'):
                        operandA+=expresion[i+4]+expresion[i+5]
                        operandB+=expresion[i+6:]
                    else:
                        operandA+=expresion[i+4]
                        operandB+=expresion[i+5:]
                else:
                    operandA+=expresion[i+2]
                    if(len(expresion)>= 4):
                        if(expresion[i+3]=='!'):
                            operandA+=expresion[i+3]+expresion[i+4]
                            operandB+=expresion[i+5:]
                        else:
                            operandA+=expresion[i+3]
                            operandB+=expresion[i+4:]

        else:
            #Checamos la longitud el antecedente (si tiene o no negacion) para ver si antecedente consta de un caracter o dos
            #Consecuente es todo lo que sigue después del antecedente
            if(expresion[i+1]=='!'):

                operandA+=expresion[i+1]+expresion[i+2]
                operandB+=expresion[3:]

            else:

                operandA+=expresion[i+1]
                operandB+=expresion[2:]
                

    return [operator, operandA, operandB]
