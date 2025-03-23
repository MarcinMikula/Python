# Przykład 1: Sortowanie przez scalanie (merge sort)
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])  # Dodajemy pozostałe elementy z left
    result.extend(right[j:])  # Dodajemy pozostałe elementy z right
    return result

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])   # Rekurencyjnie sortujemy lewą połowę
    right = merge_sort(lst[mid:])  # Rekurencyjnie sortujemy prawą połowę
    return merge(left, right)      # Scalamy posortowane połowy

numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_list = merge_sort(numbers)
print("Posortowana lista (merge sort):", sorted_list)  # Wyświetla [11, 12, 22, 25, 34, 64, 90]

# Przykład 2: Prosty przykład scalania dwóch posortowanych list
left = [11, 22, 34]
right = [12, 25, 64, 90]
merged = merge(left, right)
print("Scalone listy:", merged)  # Wyświetla [11, 12, 22, 25, 34, 64, 90]