# Przykład 1: Wyszukiwanie binarne – złożoność O(log n)
def binary_search(lst, target):
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 6
index = binary_search(sorted_list, target)
print("Indeks elementu", target, "to:", index)  # Wyświetla 5

# Przykład 2: Sortowanie bąbelkowe – złożoność O(n^2)
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

numbers = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(numbers)
print("Posortowana lista (bubble sort):", numbers)  # Wyświetla [11, 12, 22, 25, 34, 64, 90]

# Przykład 3: Sortowanie przez wybór – złożoność O(n^2)
def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst

numbers = [64, 34, 25, 12, 22, 11, 90]
selection_sort(numbers)
print("Posortowana lista (selection sort):", numbers)  # Wyświetla [11, 12, 22, 25, 34, 64, 90]