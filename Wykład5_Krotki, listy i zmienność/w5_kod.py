# Przykład 1: Podstawowe operacje na krotkach
t = (1, "hello", 3.14)
print(t[0])          # Wyświetla 1
print(t[1:3])        # Wyświetla ("hello", 3.14)
print(t + (4, 5))    # Wyświetla (1, "hello", 3.14, 4, 5)
print(t * 2)         # Wyświetla (1, "hello", 3.14, 1, "hello", 3.14)
print(len(t))        # Wyświetla 3

# Przykład 2: Funkcja zwracająca krotkę
def divide_and_remainder(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

a, b = 17, 5
q, r = divide_and_remainder(a, b)
print("Iloraz:", q, "Reszta:", r)  # Wyświetla Iloraz: 3 Reszta: 2

# Przykład 3: Podstawowe operacje na listach
L = [1, "hello", 3.14]
L.append(42)        # Dodajemy 42 na koniec
print(L)            # Wyświetla [1, "hello", 3.14, 42]
L[1] = "world"      # Zmiana elementu
print(L)            # Wyświetla [1, "world", 3.14, 42]
L.pop()             # Usuwamy ostatni element
print(L)            # Wyświetla [1, "world", 3.14]

# Przykład 4: Iteracja i modyfikacja listy
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
print("Podwojone liczby:", numbers)  # Wyświetla [2, 4, 6, 8, 10]

# Przykład 5: Porównanie zmienności
# Krotka – próba zmiany (spowoduje błąd)
t = (1, 2, 3)
# t[0] = 10  # Błąd: krotki są niezmienne

# Lista – zmiana działa
L = [1, 2, 3]
L[0] = 10
print("Zmieniona lista:", L)  # Wyświetla [10, 2, 3]

# Przykład 6: Suma elementów listy (matematyka)
values = [10, 20, 30, 40, 50]
total = 0
for value in values:
    total = total + value
print("Suma elementów:", total)  # Wyświetla 150