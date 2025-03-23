# Przykład 1: Implementacja BFS
class Graph:
    def __init__(self):
        self.graph = {}  # Lista sąsiedztwa

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)  # Graf nieskierowany

    def bfs(self, start):
        visited = set()  # Zbiór odwiedzonych wierzchołków
        queue = [start]  # Kolejka do BFS
        visited.add(start)
        traversal = []  # Kolejność odwiedzin

        while queue:
            vertex = queue.pop(0)  # Pobieramy pierwszy wierzchołek z kolejki
            traversal.append(vertex)
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return traversal

# Testowanie BFS
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(2, 4)
print("Przechodzenie BFS od wierzchołka 0:", g.bfs(0))  # Wyświetla [0, 1, 2, 3, 4]

# Przykład 2: Znajdowanie najkrótszej ścieżki za pomocą BFS
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs_shortest_path(self, start, end):
        if start not in self.graph or end not in self.graph:
            return None

        visited = set()
        queue = [(start, [start])]  # (wierzchołek, ścieżka do niego)
        visited.add(start)

        while queue:
            vertex, path = queue.pop(0)
            if vertex == end:
                return path
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        return None  # Jeśli nie ma ścieżki

# Testowanie najkrótszej ścieżki
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(2, 4)
path = g.bfs_shortest_path(0, 4)
print("Najkrótsza ścieżka z 0 do 4:", path)  # Wyświetla [0, 2, 4]