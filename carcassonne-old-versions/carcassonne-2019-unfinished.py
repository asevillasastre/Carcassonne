#LISTA DE PIEZAS
#DISPOSICIONES PERTINENTES PARA QUE SE PUEDA JUGAR COMO INPUTS Y EL CONTEO
#DIBUJADOR

class C(object):

    def __init__(self,npiezas):
        n=npiezas*2+1
        matrix=[]
        for j in range(n):
            matrix.append([])
        for j in range(len(matrix)):
            for i in range(n):
                matrix[j].append([j,i])
        matrix[npiezas][npiezas]=[{"coord" : (3,3),"extremes" : "rcrg", "unions" : [(1,3)], "monastery" : False}]
        construcciones = [{"kind": "r", "cc" : [[(3,3),[(0,2)]]], "open" : [(3,2),(3,4)], "meeples" : []}, \
                          {"kind": "c", "cc" : [[(3,3),[]]], "open" : [(2,3)], "meeples" : []}]
        #ya añadiremos puntuaje real y potencial, número de meeples, fichas que quedan por salir etc
        return {"tab" : matrix, "cons" : construcciones}

    def rep(self):
        result = []
        for i in self["tab"]:
            new = []
            for j in i:   
                if len(j)==1:
                    new.append(j[0]["extremes"])
                else:
                    new.append(j)
            result.append(new)
        print("\n--------------------------")
        print(result)
        print("--------------------------")
    
    def exp(self):
        print("__________________________")
        print("tab:")
        for i in self["tab"]:
            for j in i:
                print(j)
        print("\ncons:")
        for i in self["cons"]:
            print(i)
        print("__________________________")
        
    
    def addpiece(self,pieza,fila,columna):
        if not C.encaja(fila,columna,pieza,self):
            print("NO ENCAJA")
        else:
            self["coord"] = (fila,columna)
            self["tab"][fila][columna]=[pieza]
        
        
            for cons in self["cons"]:
                #ACTUALIZAMOS LOS CAMINOS
                if cons["kind"]=="r":
                    cons["cc"].append([(fila,columna),"unions"])
                    for a in cons["open"]:
                        if a == (fila,columna):
                            cons["open"].pop(a)
                    
                
        
            #ACTUALIZAMOS LAS CIUDADES
        
            #ACTUALIZAMOS LOS MONASTERIOS
        
        #ANALIZAMOS SI SE HA CERRAO ALGO
    
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
            if len(self["tab"][element[0]][element[1]])!=2:
                if element == (fila+1,columna):
                    result.append((3,self["tab"][fila+1][columna][0]["extremes"][1]))
                if element == (fila-1,columna):
                    result.append((1,self["tab"][fila-1][columna][0]["extremes"][3]))
                if element == (fila,columna+1):
                    result.append((2,self["tab"][fila][columna+1][0]["extremes"][0]))
                if element == (fila,columna-1):
                    result.append((0,self["tab"][fila][columna-1][0]["extremes"][2]))
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
        for adyacente in C.adyacentes(self["tab"]):
            if C.encaja(adyacente[0],adyacente[1],pieza,self):
                result.append(adyacente)
        return result

def rotaciones(pieza):
    result=[]
    for i in range(4):
        pie = pieza
        result.append(pie)
    return result 

tab3=C.__init__(0,3)
#print(type(tab3))
#print(tab3)
#print(C.rep(tab3))
print(C.exp(tab3))
###########C.addpiece(tab3,{"coord": None,"extremes" : "cccc", "unions" : [(1,2),(2,3),(2,3),(3,4)], "monastery" : False},2,3)
#print(C.alrededores(3,4,tab3))
#print(C.alrededores(2,3,tab3))
#print(C.encaja(3,4,"rcrg",tab3))
#print(C.huecos(tab3,"cccc"))
#print(C.alrededores(2,3,tab3))
#print(C.encaja(2,2,"rgcc",tab3))
#print(C.huecos(tab3,"cccc"))
#print(tab3)
#print(C.rep(tab3))
#print(C.exp(tab3))


