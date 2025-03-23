# Przykład 1: Mutowalność list – metody modyfikujące
L = [3, 1, 4, 1, 5]
L.append(9)         # Dodajemy 9 na koniec
print("Po append:", L)  # Wyświetla [3, 1, 4, 1, 5, 9]
L.extend([2, 7])    # Rozszerzamy o listę [2, 7]
print("Po extend:", L)  # Wyświetla [3, 1, 4, 1, 5, 9, 2, 7]
L.sort()            # Sortujemy listę
print("Po sort:", L)    # Wyświetla [1, 1, 2, 3, 4, 5, 7, 9]
L.pop(2)            # Usuwamy element o indeksie 2
print("Po pop:", L)     # Wyświetla [1, 1, 3, 4, 5, 7, 9]

# Przykład 2: Modyfikacja listy w funkcji
def modify_list(lst):
    lst.append(100)
    print("Wewnątrz funkcji:", lst)

L = [1, 2, 3]
modify_list(L)
print("Po wywołaniu funkcji:", L)  # Wyświetla [1, 2, 3, 100]

# Przykład 3: Aliasing – współdzielenie referencji
L1 = [1, 2, 3]
L2 = L1  # Aliasing – L2 wskazuje na tę samą listę co L1
L2.append(4)
print("L1 po zmianie L2:", L1)  # Wyświetla [1, 2, 3, 4]
print("L2:", L2)                # Wyświetla [1, 2, 3, 4]

# Przykład 4: Klonowanie – tworzenie niezależnej kopii
L1 = [1, 2, 3]
L2 = L1[:]  # Klonowanie za pomocą slice
L2.append(4)
print("L1 po klonowaniu:", L1)  # Wyświetla [1, 2, 3]
print("L2 po klonowaniu:", L2)  # Wyświetla [1, 2, 3, 4]

# Przykład 5: Obliczanie średniej elementów listy (matematyka)
numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total = total + num
average = total / len(numbers)
print("Średnia:", average)  # Wyświetla 30.0