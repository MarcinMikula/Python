# Przykład 1: Prosta tablica haszująca z łańcuchowaniem
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]  # Tworzymy listę list (łańcuchowanie)

    def hash_function(self, key):
        return hash(key) % self.size  # Prosta funkcja haszująca

    def insert(self, key, value):
        index = self.hash_function(key)
        for item in self.table[index]:
            if item[0] == key:  # Aktualizujemy, jeśli klucz już istnieje
                item[1] = value
                return
        self.table[index].append([key, value])  # Dodajemy nową parę

    def search(self, key):
        index = self.hash_function(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        return None

# Testowanie tablicy haszującej
ht = HashTable(5)
ht.insert("apple", 10)
ht.insert("banana", 20)
ht.insert("orange", 30)
print("Wartość dla 'apple':", ht.search("apple"))  # Wyświetla 10
print("Wartość dla 'banana':", ht.search("banana"))  # Wyświetla 20
print("Wartość dla 'grape':", ht.search("grape"))  # Wyświetla None

# Przykład 2: Użycie słownika do zliczania wystąpień
text = "hello world hello python"
word_count = {}
for word in text.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print("Wystąpienia słów:", word_count)  # Wyświetla {'hello': 2, 'world': 1, 'python': 1}

# Przykład 3: Porównanie wyszukiwania (konceptualne)
# Wyszukiwanie liniowe (O(n))
def linear_search(lst, key):
    for i in range(len(lst)):
        if lst[i][0] == key:
            return lst[i][1]
    return None

data = [["apple", 10], ["banana", 20], ["orange", 30]]
print("Wyszukiwanie liniowe - 'banana':", linear_search(data, "banana"))  # Wyświetla 20

# Wyszukiwanie w słowniku (O(1))
data_dict = {"apple": 10, "banana": 20, "orange": 30}
print("Wyszukiwanie w słowniku - 'banana':", data_dict["banana"])  # Wyświetla 20