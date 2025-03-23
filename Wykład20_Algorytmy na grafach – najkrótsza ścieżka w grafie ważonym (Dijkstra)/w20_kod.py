# Przykład 1: Implementacja algorytmu Dijkstry
import heapq

class Graph:
    def __init__(self):
        self.graph = {}  # Lista sąsiedztwa: {wierzchołek: [(sąsiad, waga), ...]}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))  # Dodajemy krawędź u -> v z wagą
        self.graph[v].append((u, weight))  # Graf nieskierowany

    def dijkstra(self, start):
        # Inicjalizacja odległości
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[start] = 0
        # Kolejka priorytetowa: (odległość, wierzchołek)
        pq = [(0, start)]
        # Śledzenie poprzedników do odtworzenia ścieżki
        previous = {vertex: None for vertex in self.graph}

        while pq:
            current_distance, current_vertex = heapq.heappop(pq)

            # Jeśli odległość w kolejce jest większa niż znana, pomijamy
            if current_distance > distances[current_vertex]:
                continue

            # Przeglądamy sąsiadów
            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight

                # Jeśli znaleźliśmy krótszą ścieżkę
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_vertex
                    heapq.heappush(pq, (distance, neighbor))

        return distances, previous

    def get_path(self, start, end, previous):
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = previous[current]
        return path[::-1]  # Odwracamy ścieżkę

# Testowanie algorytmu Dijkstry
g = Graph()
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 8)
g.add_edge(1, 2, 2)
g.add_edge(1, 3, 5)
g.add_edge(2, 3, 5)
g.add_edge(2, 4, 9)
g.add_edge(3, 4, 4)

distances, previous = g.dijkstra(0)
print("Odległości od wierzchołka 0:", distances)  # Wyświetla {0: 0, 1: 4, 2: 6, 3: 9, 4: 13}
path = g.get_path(0, 4, previous)
print("Najkrótsza ścieżka z 0 do 4:", path)  # Wyświetla [0, 1, 2, 3, 4]