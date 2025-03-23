# Przykład 1: Obliczanie ciągu Fibonacciego – rekurencja naiwna
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

# Przykład 2: Obliczanie ciągu Fibonacciego – DP z memoizacją (top-down)
def fib_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

# Przykład 3: Obliczanie ciągu Fibonacciego – DP z tablicowaniem (bottom-up)
def fib_tabulation(n):
    if n <= 1:
        return n
    table = [0] * (n + 1)
    table[1] = 1
    for i in range(2, n + 1):
        table[i] = table[i-1] + table[i-2]
    return table[n]

# Testowanie różnych metod
n = 10
print(f"Fibonacci({n}) - rekurencja:", fib_recursive(n))  # Wyświetla 55
print(f"Fibonacci({n}) - memoizacja:", fib_memo(n))  # Wyświetla 55
print(f"Fibonacci({n}) - tablicowanie:", fib_tabulation(n))  # Wyświetla 55

# Przykład 4: Porównanie czasów wykonania
import time

def measure_time(func, n):
    start = time.time()
    result = func(n)
    end = time.time()
    return result, end - start

n = 35
result1, time1 = measure_time(fib_recursive, n)
result2, time2 = measure_time(fib_memo, n)
result3, time3 = measure_time(fib_tabulation, n)

print(f"\nPorównanie czasów dla n={n}:")
print(f"Rekurencja: {result1}, czas: {time1:.4f} sekund")
print(f"Memoizacja: {result2}, czas: {time2:.4f} sekund")
print(f"Tablicowanie: {result3}, czas: {time3:.4f} sekund")