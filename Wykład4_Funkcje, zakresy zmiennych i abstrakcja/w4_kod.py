# Przykład 1: Funkcja obliczająca kwadrat liczby
def square(x):
    return x * x

num = 4
result = square(num)
print("Kwadrat liczby", num, "to:", result)  # Wyświetla 16

# Przykład 2: Funkcja sprawdzająca parzystość
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

number = 6
if is_even(number):
    print(number, "jest parzyste")
else:
    print(number, "jest nieparzyste")  # Wyświetla "6 jest parzyste"

# Przykład 3: Funkcja aproksymująca pierwiastek kwadratowy
def sqrt_approx(y, epsilon=0.01, krok=0.1):
    x = 0
    licznik_krokow = 0
    while x * x <= y:
        if abs(x * x - y) < epsilon:
            return x, licznik_krokow
        x = x + krok
        licznik_krokow = licznik_krokow + 1
    return None, licznik_krokow  # Zwraca None, jeśli nie znaleziono wyniku

y = 25
result, steps = sqrt_approx(y)
if result is not None:
    print("Przybliżony pierwiastek z", y, "to:", result)
    print("Liczba kroków:", steps)  # Wyświetla 5.0, 50 kroków
else:
    print("Nie znaleziono pierwiastka")

# Przykład 4: Zakres zmiennych – zmienna lokalna
def test_scope():
    local_var = 10
    print("Wewnątrz funkcji:", local_var)

test_scope()
# print(local_var)  # Błąd – local_var nie jest dostępna poza funkcją

# Przykład 5: Funkcja z wieloma parametrami
def add_and_multiply(a, b, c):
    return (a + b) * c

result = add_and_multiply(2, 3, 4)
print("Wynik (2 + 3) * 4:", result)  # Wyświetla 20