# Przykład 1: Implementacja grafu za pomocą listy sąsiedztwa
class Graph:
    def __init__(self):
        self.graph = {}  # Słownik przechowujący listę sąsiedztwa

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)  # Dodajemy krawędź u -> v
        self.graph[v].append(u)  # Dodajemy krawędź v -> u (graf nieskierowany)

    def display(self):
        for vertex in self.graph:
            print(f"{vertex}: {self.graph[vertex]}")

# Testowanie grafu
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.display()  # Wyświetla:
# 0: [1, 2]
# 1: [0, 2, 3]
# 2: [0, 1, 3]
# 3: [1, 2]

# Przykład 2: Przeszukiwanie w głąb (DFS)
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

    def dfs(self, start):
        visited = set()  # Zbiór odwiedzonych wierzchołków
        traversal = []   # Lista przechowująca kolejność odwiedzin
        self._dfs_recursive(start, visited, traversal)
        return traversal

    def _dfs_recursive(self, vertex, visited, traversal):
        visited.add(vertex)
        traversal.append(vertex)
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited, traversal)

# Testowanie DFS
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
print("Przechodzenie DFS od wierzchołka 0:", g.dfs(0))  # Wyświetla [0, 1, 2, 3]