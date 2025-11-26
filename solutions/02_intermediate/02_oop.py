"""
Solution 5: Object-Oriented Programming
========================================
"""

# Exercise 5.1: Basic class
class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
    
    def bark(self):
        print(f"{self.name} says Woof!")

my_dog = Dog("Buddy", "Golden Retriever", 3)
my_dog.bark()

# Exercise 5.2: Class with properties
class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount}. New balance: ${self._balance}")
        else:
            print("Deposit amount must be positive")
    
    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient funds")
        elif amount <= 0:
            print("Withdrawal amount must be positive")
        else:
            self._balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self._balance}")
    
    def get_balance(self):
        return self._balance

print("\nBank Account:")
account = BankAccount(100)
account.deposit(50)
account.withdraw(30)
print(f"Final balance: ${account.get_balance()}")

# Exercise 5.3: Inheritance
class Animal:
    def speak(self):
        pass

class Cat(Animal):
    def speak(self):
        print("Meow!")

class Bird(Animal):
    def speak(self):
        print("Chirp!")

print("\nAnimals:")
cat = Cat()
bird = Bird()
cat.speak()
bird.speak()

# Exercise 5.4: Class methods and static methods
class MathOperations:
    pi = 3.14159
    
    @staticmethod
    def add(a, b):
        return a + b
    
    @classmethod
    def circle_area(cls, radius):
        return cls.pi * radius ** 2

print("\nMath Operations:")
print(f"5 + 3 = {MathOperations.add(5, 3)}")
print(f"Area of circle with radius 5: {MathOperations.circle_area(5):.2f}")

# Exercise 5.5: Magic methods
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

print("\nVectors:")
v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2
print(f"{v1} + {v2} = {v3}")
print(f"v1 == v2: {v1 == v2}")
print(f"v1 == v1: {v1 == v1}")
