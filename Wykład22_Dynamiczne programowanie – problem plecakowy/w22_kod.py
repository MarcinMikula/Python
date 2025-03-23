# Przykład 1: Problem plecakowy 0-1 za pomocą dynamicznego programowania
def knapsack_01(values, weights, capacity):
    n = len(values)  # Liczba przedmiotów
    # Tworzymy tablicę DP: dp[i][w] to maksymalna wartość dla i przedmiotów i pojemności w
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Wypełniamy tablicę DP
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:  # Jeśli przedmiot mieści się w plecaku
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - weights[i-1]] + values[i-1])
            else:  # Jeśli się nie mieści, bierzemy wartość bez tego przedmiotu
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]

# Przykład 2: Odtwarzanie wybranego podzbioru przedmiotów
def knapsack_01_with_items(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Wypełniamy tablicę DP
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]

    # Odtwarzamy wybrane przedmioty
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:  # Jeśli przedmiot i-1 został wybrany
            selected_items.append(i-1)
            w -= weights[i-1]

    return dp[n][capacity], selected_items

# Testowanie problemu plecakowego
values = [60, 100, 120]  # Wartości przedmiotów
weights = [10, 20, 30]   # Wagi przedmiotów
capacity = 50            # Pojemność plecaka

# Testowanie wersji podstawowej
max_value = knapsack_01(values, weights, capacity)
print(f"Maksymalna wartość (bez przedmiotów): {max_value}")  # Wyświetla 220

# Testowanie wersji z odtwarzaniem przedmiotów
max_value, items = knapsack_01_with_items(values, weights, capacity)
print(f"Maksymalna wartość: {max_value}, Wybrane przedmioty (indeksy): {items}")  # Wyświetla 220, [2, 1]