import random

class Graph(object):

    def __init__(self, graph_dict=None):
        if graph_dict == None:
            graph_dict = {}
        self._graph_dict = graph_dict

    def edges(self, vertice): # this one is the link
        return self._graph_dict[vertice]

    def all_vertices(self):
        return set(self._graph_dict.keys())

    def all_edges(self):
        return self.__generate_edges()

    def add_vertex(self, vertex):
        if vertex not in self._graph_dict:
            self._graph_dict[vertex] = []

    def add_edge(self, edge):
        edge = set(edge)
        vertex1, vertex2 = tuple(edge)
        for x, y in [(vertex1, vertex2), (vertex2, vertex1)]:
            if x in self._graph_dict:
                self._graph_dict[x].add(y)
            else:
                self._graph_dict[x] = [y]

    def __generate_edges(self):
        edges = []
        for vertex in self._graph_dict:
            for neighbour in self._graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __iter__(self):
        self._iter_obj = iter(self._graph_dict)
        return self._iter_obj

    def __next__(self):
        return next(self._iter_obj)

    def __str__(self):
        res = "vertices: "
        for k in self._graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

# Generates a random graph
def generateRandomGraph(vertices,edges):
    g = {}
    for x in range(vertices):
        a = set()
        for y in range(random.randint(1,edges)):
            t = random.randint(0,vertices-1)# node can't connect to its self
            while t == x:
                t = random.randint(0,vertices-1)
            a.add(t)
        g[x] = a

    return g

g = generateRandomGraph(8,3)
graph = Graph(g)

for vertice in graph:
    print(f"Edges of vertice {vertice}: ", graph.edges(vertice))

def assignCoordinates(gr):
    coordinate = {}
    for vertice in gr:
        
