# Przykład 1: Dziedziczenie – klasa Animal i klasy pochodne
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Nie wiem, co powiedzieć!"

class Dog(Animal):
    def speak(self):
        return f"{self.name} mówi: Hau hau!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} mówi: Miau miau!"

# Testowanie
dog = Dog("Reksio")
cat = Cat("Mruczek")
print(dog.speak())  # Wyświetla "Reksio mówi: Hau hau!"
print(cat.speak())  # Wyświetla "Mruczek mówi: Miau miau!"

# Przykład 2: Klasa Person i Student z użyciem super()
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Jestem {self.name}, mam {self.age} lat."

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Wywołujemy konstruktor klasy bazowej
        self.student_id = student_id

    def introduce(self):  # Nadpisywanie metody
        return f"Jestem {self.name}, mam {self.age} lat, mój numer studenta to {self.student_id}."

# Testowanie
person = Person("Jan", 30)
student = Student("Anna", 20, "12345")
print(person.introduce())  # Wyświetla "Jestem Jan, mam 30 lat."
print(student.introduce())  # Wyświetla "Jestem Anna, mam 20 lat, mój numer studenta to 12345."

# Przykład 3: Figury geometryczne – obliczanie pola
class Shape:
    def area(self):
        return 0  # Metoda bazowa, do nadpisywania

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Testowanie
circle = Circle(5)
rectangle = Rectangle(4, 6)
print("Pole koła:", circle.area())  # Wyświetla 78.5
print("Pole prostokąta:", rectangle.area())  # Wyświetla 24