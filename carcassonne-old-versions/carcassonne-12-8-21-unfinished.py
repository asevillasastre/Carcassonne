"""
#######################################
######### CARCASSONNE 12/8/21 #########
#######################################
"""

class Game(object):
    
    def __init__(self, board_dimension):
        self.board = Board(board_dimension)
        self.buildings = Buildings()

class Board(object):
    
    def __init__(self, dimension):
        m = []
        for j in range(dimension):
            m.append([])
        for j in range(len(m)):
            for i in range(dimension):
                m[j].append([])
        print(m)
        self.matrix = m
    
    def __repr__(self):
        dim = len(self.matrix)
        result = []
        for x in range(dim * 3):
            result.append("\n")
            for y in range(dim * 3):
                if self.matrix[x//3][y//3] != []:
                    result.append(" .")
                else:
                    result.append(" *")
        
        draw = ""
        for i in range(len(result)):
            draw += result[i]
        
        return draw

class Buildings(object):
    
    def __init__(self):
        self.roads = []
        self.castles = []
        self.monasteries = []
        self.fields = []

class Road(object):
    
    def __init__(self, edges, path, meeples):
        """
        edges: list of range 2!!!!!!!!!!!!
        path: list of pieces with road and its unions saved as Road_stretch objects
        meeples: list of meeples
        """
        self.edges = edges
        self.path = path
        self.meeples = meeples

class Road_stretch(object):
    
    def __init__(self, coordinates, unions):
        """
        coordinates: list of range 2
        unions: list of unions of edges. example: [((0, 0), (2, 0))] el recto de izda a dcha ubicado en (1, 0), +
        + example: [((0, 1), "end"), ((1, 0), "end"), ((1, 2), "end"), ((2, 1), "end"),] el cruce de 4 caminos ubicado en (1, 1)
        #ten en cuenta las ciudades y caminos con puente q el camino pasa por el mismo lao 2 veces, +
        # + tiene q ponerse 2 uniones en la misma coordenada 
        """
        self.coordinates = coordinates
        self.unions = unions

class Castle(object):
    
    def __init__(self, edges, courtyard, meeples, shields):
        """
        edges: list of any range!!!!!!!!!!!!!
        courtyard: list of pieces with road and its unions saved as Castle_stretch objects
        meeples: list of meeples
        """
        self.edges = edges
        self.courtyard = courtyard
        self.meeples = meeples
        self.shields = shields

class Castle_stretch(object):
    
    def __init__(self, coordinates, unions):
        """
        coordinates: list of range 2
        unions: list of unions of edges. example: [((0, 0), (2, 0))] el pasillo de izda a dcha ubicado en (1, 0), +
        [((0, 1),(2, 1),(1, 2),(1, 0))] la catedral en (1, 1) LAS COMPONENTES CONEXAS METERLAS EN UNA MISMA LISTA
        #ten en cuenta las ciudades y caminos con puente q el camino pasa por el mismo lao 2 veces, +
        # + tiene q ponerse 2 uniones en la misma coordenada 
        """
        self.coordinates = coordinates
        self.unions = unions

class Monastery(object):
    
    def __init__(self, edges, meeples):
        """
        edges: list of range 0-9!!!!!!!!!!!!!
        meeples: list of meeples
        """
        self.edges = edges
        self.meeples = meeples

class Field(object):
    
    def __init__(self, edges, pasture, meeples, castles):
        """
        edges: list of any range!!!!!!!!!!!!!
        pasture: list of pieces with road and its unions saved as Field_stretch objects
        meeples: list of meeples
        castles: list of Castle objects 
        """
        self.edges = edges
        self.pasture = pasture
        self.meeples = meeples
        self.castles = castles

class Field_stretch(object):
    
    def __init__(self, coordinates, unions):
        """
        coordinates: list of range 2
        unions: list of unions of edges. +
        + example: [[(0, 0, 4), "end"], [(0, 0, 5), "end"]] la ciudad trigrande sin camino en (1, 0) +
        + example: [[(0, 0, 2), "end"], [(0, 0, 3), "end"]] la ciudad trigrande sin camino en (0, 1) +
        + example: [[(0, 1, 4), (1, 2, 6), (1, 2, 7), (2, 1, 1)] la parte de arriba del camino recto de izda a dcha en (1, 1) +
        + example: [(0, 1, 5), (1, 0, 2), (1, 0, 3), (2, 1, 0)]] la parte de abajo del camino recto de izda a dcha en (1, 1)
        #ten en cuenta las ciudades y caminos con puente q el camino pasa por el mismo lao 2 veces, +
        # + tiene q ponerse 2 uniones en la misma coordenada
        """
        self.coordinates = coordinates
        self.unions = unions

class Piece():
    
    def __init__(self, edges, roads, castles, monasteries, fields):
        """
        edges = "rfrc"
        roads = [[0, "end"], [1, 2]]
        castles = [[[0, 1], True], [[2, "end"], False]]
        monasteries = True
        fields = [[1,2,3,4], [0,5,6,7]]
        """
        self.edges = edges
        self.roads = roads
        self.castles = castles
        self.monasteries = monasteries
        self.fields = fields
        return None

    def rotate(self):
        self.edges = self.edges[3] + self.edges[0] + self.edges[1] + self.edges[2]
    
    def __repr__(self):
        
        result = list("...\n...\n...")
        
        if self.edges[0] == "r":
            result[4] = "_"
        if self.edges[2] == "r":
            result[6] = "_"
        if self.edges[1] == "r":
            result[1] = "|"
        if self.edges[3] == "r":
            result[9] = "|"
            
        if self.edges[0] == "c":
            result[0], result[4], result[8] = "c", "c", "c"
        if self.edges[2] == "c":
            result[2], result[6], result[10] = "c", "c", "c"
        if self.edges[1] == "c":
            result[0], result[1], result[2] = "c", "c", "c"
        if self.edges[3] == "c":
            result[8], result[9], result[10] = "c", "c", "c"
            
        if self.monasteries:
            result[5] = "+"
        
        #print(result)
        draw = ""
        for i in range(len(result)):
            draw += " "
            draw += result[i]

        
        return draw

####
game1 = Game(3)
piece1 = Piece("rcrf", [[0, 2]], [[[1, "end"], False]], False, [[1,2,3,4], [0,5,6,7]])
piece2 = Piece("cccf", [], [[[0, 1, 2, "end"], True]], False, [[6,7]])
piece3 = Piece("fffr", [[0, 2]], [], True, [[0,1,2,3,4,5,6,7]])
#print(piece1)
#print(piece2)
#print(piece3)
board1 = Board(5)
print(board1)


