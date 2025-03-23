# Przykład 1: Podstawowe operacje na stringach
s = "hello"
print(s[0])          # Wyświetla "h"
print(s[1:4])        # Wyświetla "ell"
print(s + " world")  # Wyświetla "hello world"
print(s * 2)         # Wyświetla "hellohello"
print(len(s))        # Wyświetla 5

# Przykład 2: Wejście i wyjście – powitanie użytkownika
name = input("Podaj swoje imię: ")
greeting = "Cześć, " + name + "!"
print(greeting)

# Przykład 3: Iteracja po stringu – zliczanie samogłosek
word = "python"
vowels = "aeiou"
count = 0
for char in word:
    if char in vowels:
        count = count + 1
print("Liczba samogłosek w", word, "to:", count)  # Wyświetla 2

# Przykład 4: Kodowanie znaków (ASCII) i proste szyfrowanie
char = "a"
print(ord(char))  # Wyświetla 97
print(chr(97))    # Wyświetla "a"

# Szyfrowanie: przesunięcie o 1
text = "hello"
encrypted = ""
for char in text:
    code = ord(char)
    encrypted = encrypted + chr(code + 1)
print("Zaszyfrowany tekst:", encrypted)  # Wyświetla "ifmmp"

# Przykład 5: Konwersja typów z wejścia
number = int(input("Podaj liczbę: "))
result = number * 2
print("Podwojona liczba to:", result)