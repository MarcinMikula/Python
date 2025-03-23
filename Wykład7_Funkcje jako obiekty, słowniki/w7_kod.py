# Przykład 1: Funkcje jako obiekty – przekazywanie funkcji jako argumentu
def square(x):
    return x * x

def apply_function(func, value):
    return func(value)

num = 5
result = apply_function(square, num)
print("Kwadrat", num, "to:", result)  # Wyświetla 25

# Przykład 2: Użycie map() do stosowania funkcji na liście
numbers = [1, 2, 3, 4, 5]
squared = list(map(square, numbers))
print("Kwadraty liczb:", squared)  # Wyświetla [1, 4, 9, 16, 25]

# Przykład 3: Podstawowe operacje na słownikach
d = {"a": 1, "b": 2, "c": 3}
print(d["a"])        # Wyświetla 1
d["d"] = 4           # Dodajemy nową parę
print(d)             # Wyświetla {"a": 1, "b": 2, "c": 3, "d": 4}
d.pop("b")           # Usuwamy parę o kluczu "b"
print(d)             # Wyświetla {"a": 1, "c": 3, "d": 4}

# Przykład 4: Zliczanie wystąpień liter w stringu
text = "hello"
letter_count = {}
for char in text:
    if char in letter_count:
        letter_count[char] = letter_count[char] + 1
    else:
        letter_count[char] = 1
print("Wystąpienia liter:", letter_count)  # Wyświetla {"h": 1, "e": 1, "l": 2, "o": 1}

# Przykład 5: Słownik jako funkcja matematyczna (f(x) = x^2)
square_dict = {}
for x in range(1, 6):
    square_dict[x] = x * x
print("Słownik f(x) = x^2:", square_dict)  # Wyświetla {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print("f(3) =", square_dict[3])  # Wyświetla 9