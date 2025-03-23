# Przykład 1: Obliczanie średniej i odchylenia standardowego
import math

def mean(data):
    return sum(data) / len(data)

def std_dev(data):
    mu = mean(data)
    n = len(data)
    variance = sum((x - mu) ** 2 for x in data) / n
    return math.sqrt(variance)

# Testowanie na prostym zbiorze danych
data = [1, 2, 3, 4, 5]
print(f"Dane: {data}")
print(f"Średnia: {mean(data)}")  # Wyświetla 3.0
print(f"Odchylenie standardowe: {std_dev(data):.2f}")  # Wyświetla 1.41

# Przykład 2: Generowanie danych z rozkładem normalnym
import random

def generate_normal_data(mu, sigma, n):
    return [random.gauss(mu, sigma) for _ in range(n)]

# Generowanie i analiza danych
mu = 0    # Średnia rozkładu normalnego
sigma = 1  # Odchylenie standardowe
n = 1000  # Liczba próbek

normal_data = generate_normal_data(mu, sigma, n)
print(f"\nWygenerowane dane (pierwsze 5): {normal_data[:5]}")
print(f"Średnia wygenerowanych danych: {mean(normal_data):.2f}")
print(f"Odchylenie standardowe wygenerowanych danych: {std_dev(normal_data):.2f}")