# Przykład 1: Wyszukiwanie liniowe – złożoność O(n)
def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
target = 5
index = linear_search(numbers, target)
print("Indeks elementu", target, "to:", index)  # Wyświetla 4

# Przykład 2: Obliczanie silni – iteracyjnie (O(n))
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

n = 5
print("Silnia (iteracyjnie) z", n, "to:", factorial_iterative(n))  # Wyświetla 120

# Przykład 3: Obliczanie silni – rekurencyjnie (O(n))
def factorial_recursive(n):
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)

n = 5
print("Silnia (rekurencyjnie) z", n, "to:", factorial_recursive(n))  # Wyświetla 120

# Przykład 4: Pętla zagnieżdżona – złożoność O(n^2)
def nested_loop_example(n):
    count = 0
    for i in range(n):
        for j in range(n):
            count = count + 1
    return count

n = 4
operations = nested_loop_example(n)
print("Liczba operacji dla n =", n, "to:", operations)  # Wyświetla 16