# Przykład 1: Rozgałęzienia – sprawdzanie, czy liczba jest dodatnia, ujemna czy zero
x = 5
if x > 0:
    print(x, "jest dodatnie")
elif x < 0:
    print(x, "jest ujemne")
else:
    print(x, "jest równe zero")

# Przykład 2: Pętla while – sumowanie liczb od 1 do 5
suma = 0
i = 1
while i <= 5:
    suma = suma + i
    i = i + 1
print("Suma liczb od 1 do 5 wynosi:", suma)  # Wyświetla 15

# Przykład 3: Pętla for – iteracja po zakresie liczb
for j in range(1, 6):
    print("Liczba:", j)

# Przykład 4: Aproksymacja pierwiastka kwadratowego metodą prób i błędów
y = 25
x = 0
krok = 0.1
epsilon = 0.01  # Dokładność
licznik_krokow = 0

while x * x <= y:
    if abs(x * x - y) < epsilon:
        print("Przybliżony pierwiastek z", y, "to", x)
        print("Liczba kroków:", licznik_krokow)
        break
    x = x + krok
    licznik_krokow = licznik_krokow + 1
else:
    print("Nie znaleziono pierwiastka w zadanym zakresie")

# Przykład 5: Sprawdzanie parzystości liczby w pętli
n = 10
while n > 0:
    if n % 2 == 0:
        print(n, "jest parzyste")
    else:
        print(n, "jest nieparzyste")
    n = n - 1