# Przykład 1: Definiowanie klasy Point
class Point:
    def __init__(self, x, y):
        self.x = x  # Atrybut x
        self.y = y  # Atrybut y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance_from_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

# Tworzenie obiektów i testowanie
p1 = Point(3, 4)
print("Punkt p1:", p1.get_x(), p1.get_y())  # Wyświetla 3, 4
print("Odległość p1 od (0,0):", p1.distance_from_origin())  # Wyświetla 5.0

# Przykład 2: Metoda do obliczania odległości między punktami
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance_from_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def distance_to(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        return (dx ** 2 + dy ** 2) ** 0.5

# Testowanie odległości między punktami
p1 = Point(3, 4)
p2 = Point(0, 0)
print("Odległość między p1 a p2:", p1.distance_to(p2))  # Wyświetla 5.0

# Przykład 3: Przesunięcie punktu
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

# Testowanie przesunięcia
p = Point(1, 2)
print("Przed przesunięciem:", p.get_x(), p.get_y())  # Wyświetla 1, 2
p.move(2, 3)
print("Po przesunięciu:", p.get_x(), p.get_y())  # Wyświetla 3, 5