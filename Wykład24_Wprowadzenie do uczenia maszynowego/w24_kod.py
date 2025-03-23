# Przykład 1: Implementacja algorytmu k-NN
import math
from collections import Counter


def euclidean_distance(point1, point2):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(point1, point2)))


def knn(training_data, labels, new_point, k):
    # Obliczamy odległości do wszystkich punktów treningowych
    distances = []
    for i, point in enumerate(training_data):
        distance = euclidean_distance(point, new_point)
        distances.append((distance, labels[i]))

    # Sortujemy według odległości i wybieramy k najbliższych
    distances.sort(key=lambda x: x[0])
    k_nearest = distances[:k]

    # Wybieramy najczęstszą klasę wśród k sąsiadów
    k_labels = [label for _, label in k_nearest]
    most_common = Counter(k_labels).most_common(1)
    return most_common[0][0]


# Przykład 2: Testowanie k-NN na prostym zbiorze danych
# Dane: punkty 2D (długość, szerokość płatka), etykiety: 0 (setosa), 1 (versicolor)
training_data = [
    (5.1, 3.5),  # setosa
    (4.9, 3.0),  # setosa
    (7.0, 3.2),  # versicolor
    (6.4, 3.2),  # versicolor
]
labels = [0, 0, 1, 1]

# Nowy punkt do sklasyfikowania
new_point = (6.5, 3.0)
k = 3

# Klasyfikacja
predicted_label = knn(training_data, labels, new_point, k)
print(f"Nowy punkt: {new_point}, Przewidywana klasa: {predicted_label}")  # Wyświetla 1 (versicolor)

# Testowanie na kilku punktach
test_points = [(5.0, 3.4), (6.7, 3.1)]
for point in test_points:
    predicted_label = knn(training_data, labels, point, k)
    print(f"Punkt: {point}, Przewidywana klasa: {predicted_label}")