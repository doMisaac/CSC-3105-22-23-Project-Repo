# Q 2(b,i)

#developing undirected graph data structure 

class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)  

    def display(self):
        for vertex in self.graph:
            print(vertex, "-->", " --> ".join(map(str, self.graph[vertex])))