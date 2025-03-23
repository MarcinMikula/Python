# Przykład 1: Implementacja klasy Stack (stosu)
class Stack:
    def __init__(self):
        self.items = []  # Lista przechowująca elementy stosu

    def push(self, item):
        self.items.append(item)  # Dodajemy element na koniec listy

    def pop(self):
        if not self.is_empty():
            return self.items.pop()  # Usuwamy i zwracamy ostatni element
        return None

    def is_empty(self):
        return len(self.items) == 0

# Testowanie stosu
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Stos po dodaniu:", stack.items)  # Wyświetla [1, 2, 3]
print("Pop:", stack.pop())  # Wyświetla 3
print("Stos po pop:", stack.items)  # Wyświetla [1, 2]

# Przykład 2: Implementacja klasy Queue (kolejki)
class Queue:
    def __init__(self):
        self.items = []  # Lista przechowująca elementy kolejki

    def enqueue(self, item):
        self.items.append(item)  # Dodajemy element na koniec listy

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)  # Usuwamy i zwracamy pierwszy element
        return None

    def is_empty(self):
        return len(self.items) == 0

# Testowanie kolejki
queue = Queue()
queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")
print("Kolejka po dodaniu:", queue.items)  # Wyświetla ['A', 'B', 'C']
print("Dequeue:", queue.dequeue())  # Wyświetla A
print("Kolejka po dequeue:", queue.items)  # Wyświetla ['B', 'C']

# Przykład 3: Użycie stosu do odwracania listy
def reverse_list(lst):
    stack = Stack()
    for item in lst:
        stack.push(item)
    reversed_list = []
    while not stack.is_empty():
        reversed_list.append(stack.pop())
    return reversed_list

# Testowanie odwracania listy
lst = [1, 2, 3, 4, 5]
reversed_lst = reverse_list(lst)
print("Oryginalna lista:", lst)  # Wyświetla [1, 2, 3, 4, 5]
print("Odwrócona lista:", reversed_lst)  # Wyświetla [5, 4, 3, 2, 1]