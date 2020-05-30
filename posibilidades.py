class Posibilidades:
    def __init__(self):
        self.lista=[]
        self.iterator = 0
    
    def insertValue(self,lista):
            self.lista.append(lista)

    def getNumPosibl(self):
        return len(self.lista)

    def incrementIterator(self):
        self.iterator = self.iterator + 1
    
    def getPosibilities(self):
        return self.lista