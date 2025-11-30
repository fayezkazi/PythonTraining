"""
Solution 8: Generators and Iterators
=====================================
"""

# Exercise 8.1: Basic generator
def number_generator(n):
    for i in range(1, n + 1):
        yield i

print("Numbers from 1 to 5:")
for num in number_generator(5):
    print(num, end=" ")
print()

# Exercise 8.2: Fibonacci generator
def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

print("\nFirst 10 Fibonacci numbers:")
for num in fibonacci(10):
    print(num, end=" ")
print()

# Exercise 8.3: Generator expressions
squares_gen = (x ** 2 for x in range(1, 11))
print("\nSquares using generator expression:")
for square in squares_gen:
    print(square, end=" ")
print()

# Exercise 8.4: Custom iterator
class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

print("\nCountdown from 5:")
for num in Countdown(5):
    print(num, end=" ")
print()

# Exercise 8.5: Infinite generator
def even_numbers():
    num = 0
    while True:
        yield num
        num += 2

print("\nFirst 10 even numbers:")
gen = even_numbers()
for _ in range(10):
    print(next(gen), end=" ")
print()
