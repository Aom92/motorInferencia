def my_range(start, end, step):
    while start>=end:
        yield start
        start += step

"""
    @brief Funcion que se encarga de encontrar la operacion mas externa dentro de una expresion logica
    @param La expresion a revisar
    @return Una tupla con el indice en donde se encuentra el operador dentro de la expresion y el operador
"""
def getExternal(expresion):
    numParentesis=0
    #if(expresion[0]=='(' and expresion[len(expresion)-1] == ')'):
        #print("verga")
        #expresion = expresion[1:]
        #expresion = expresion[:len(expresion)-1]
    #print(expresion)
    #Iteramos la expresion revisando sus caracteres
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
    @brief Funcion que se encarga de dividir la expresion logica en [antes de operador, operador, despues de operador]
    @param La expresion a revisar
    @return Lista con los elementos de la operacion en caso de haber una o 0 en caso de no haberlo
"""
def getElements(expresion):
    external=getExternal(expresion)
    if(external!=0):
        val=external[1]
        left=expresion[:external[0]]
        right=expresion[external[0]+1:]

        if(left[0]=='(' and left[len(left)-1]==')'):
            left=left[1:]
            left=left[:len(left)-1]
        if(right[0]=='(' and right[len(right)-1]==')'):
            right=right[1:]
            right=right[:len(right)-1]

        lista = [left,external[1],right]
        return lista
    return 0

def getElementsPrefix(expresion):
    iterator = len(expresion)-1
    operator=''
    operandA=''
    operandB=''
    operation=[]
    if(len(expresion)<=2):
        return [expresion]
    
    i = 0

    if(expresion[i]=='^' or expresion[i]=='v' or expresion[i]=='>'):
        operator+=expresion[i]
        if(expresion[i+1]=='^' or expresion[i+1]=='v' or expresion[i+1]=='>'):
            if(expresion[i+2]=='^' or expresion[i+2]=='v' or expresion[i+2]=='>'):
                operandA=expresion[i+1]+expresion[i+2]

                acum = 0
                desplazamiento = 0
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

            if(expresion[i+1]=='!'):

                operandA+=expresion[i+1]+expresion[i+2]
                operandB+=expresion[3:]

            else:

                operandA+=expresion[i+1]
                operandB+=expresion[2:]
                

    return [operator, operandA, operandB]
