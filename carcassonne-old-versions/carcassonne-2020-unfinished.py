class C(object):

    def __init__(self,npiezas):
        n=npiezas*2+1
        matrix=[]
        for j in range(n):
            matrix.append([])
        for j in range(len(matrix)):
            for i in range(n):
                matrix[j].append([j,i])
        matrix[npiezas][npiezas]=[{"extremes" : "rcrg", "unions" : [(1,3)], "monastery" : False}]
        return matrix

    def rep(self):
        result = []
        for i in self:
            new = []
            for j in i:    
                if len(j)==1:
                    new.append(j[0]["extremes"])
                else:
                    new.append(j)
            result.append(new)
        return result
    
    def addpiece(self,pieza,fila,columna):
        self[fila][columna]=[pieza]
    
    def adyacentes(self):
        result=[]
        for fila in range(len(self)):
            for columna in range(len(self)):
                if len(self[fila][columna])!=2:
                    for element in [(fila+1,columna),(fila-1,columna),(fila,columna+1),(fila,columna-1)]:
                        if len(self[element[0]][element[1]])==2 and element not in result:
                            result.append(element)
        return result
    
    def alrededores(fila,columna,self):
        result=[]
        for element in [(fila+1,columna),(fila-1,columna),(fila,columna+1),(fila,columna-1)]:
            if len(self[element[0]][element[1]])!=2:
                if element == (fila+1,columna):
                    result.append((3,self[fila+1][columna][0][1]))
                if element == (fila-1,columna):
                    result.append((1,self[fila-1][columna][0][3]))
                if element == (fila,columna+1):
                    result.append((2,self[fila][columna+1][0][0]))
                if element == (fila,columna-1):
                    result.append((0,self[fila][columna-1][0][2]))
        return result
    
    def encaja(fila,columna,pieza,self):
        requisitos=C.alrededores(fila,columna,self)
        result=False
        for rotacion in rotaciones(pieza):
            paece=True
            for requisito in requisitos:
                if rotacion[requisito[0]]!=requisito[1]:
                    paece=False
                    break
            if paece==True:
                return True
        return result

    def huecos(self,pieza):
        result=[]
        for adyacente in C.adyacentes(self):
            if C.encaja(adyacente[0],adyacente[1],pieza,self):
                result.append(adyacente)
        return result

def rotaciones(pieza):
    result=[]
    for i in range(len(pieza)):
        pie=[]
        j=0
        while j<len(pieza):
            pie.append(pieza[(i+j)%len(pieza)])
            j+=1
        result.append(pie)
    return result 

tab3=C.__init__(0,3)
print(type(tab3))
print(tab3)

print("----------------------------")
C.addpiece(tab3,{"extremes" : "cccc", "unions" : [(1,2),(2,3),(2,3),(3,4)], "monastery" : False},2,4)

print(C.rep(tab3))
"""
print("----------------------------")
print(C.alrededores(3,4,tab3))
print("----------------------------")
print(C.encaja(3,4,"rcrg",tab3))
print("----------------------------")
print(C.huecos(tab3,"cccc"))
print("----------------------------")
print(tab3)
print("----------------------------")
C.addpiece(tab3,["cccc",[(1,3),(1,2),(1,3),(1,4),],[2],False],3,2)
C.addpiece(tab3,["rrrr",[(1,3)],[2],False],2,3)
print(tab3)
print("----------------------------")

print(C.alrededores(2,3,tab3))

print(C.encaja(2,2,"rgcc",tab3))

print(C.huecos(tab3,"cccc"))

print(tab3)
"""

