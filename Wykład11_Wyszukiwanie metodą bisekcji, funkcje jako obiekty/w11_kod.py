# Przykład 1: Wyszukiwanie metodą bisekcji – pierwiastek kwadratowy
def sqrt_bisection(y, epsilon=0.01):
    low = 0
    high = y
    guess = (low + high) / 2
    steps = 0
    while abs(guess * guess - y) >= epsilon:
        steps += 1
        if guess * guess < y:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2
    return guess, steps

y = 25
result, steps = sqrt_bisection(y)
print("Pierwiastek z", y, "to około:", result)
print("Liczba kroków:", steps)  # Wyświetla około 5.0, 11 kroków

# Przykład 2: Ogólna metoda bisekcji z funkcją jako argumentem
def bisection_solver(func, a, b, epsilon=0.01):
    if func(a) * func(b) >= 0:
        return None, 0  # Funkcja musi zmieniać znak na przedziale
    steps = 0
    while (b - a) >= epsilon:
        steps += 1
        mid = (a + b) / 2
        if func(mid) == 0:
            return mid, steps
        elif func(mid) * func(a) < 0:
            b = mid
        else:
            a = mid
    return (a + b) / 2, steps

# Funkcja do rozwiązania: x^2 - 25 = 0
def f(x):
    return x * x - 25

root, steps = bisection_solver(f, 0, 10)
print("Rozwiązanie x^2 - 25 = 0:", root)
print("Liczba kroków:", steps)  # Wyświetla około 5.0, 10 kroków

# Przykład 3: Prosty przykład przekazywania funkcji
def apply_function(func, value):
    return func(value)

def cube(x):
    return x * x * x

value = 3
result = apply_function(cube, value)
print("Sześcian", value, "to:", result)  # Wyświetla 27