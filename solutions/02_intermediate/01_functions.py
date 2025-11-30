"""
Solution 4: Functions
=====================
"""

from functools import reduce

# Exercise 4.1: Basic function
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# Exercise 4.2: Function with return value
def add(a, b):
    return a + b

result = add(5, 3)
print(f"\n5 + 3 = {result}")

# Exercise 4.3: Function with default parameters
def power(base, exponent=2):
    return base ** exponent

print(f"\n2^3 = {power(2, 3)}")
print(f"5^2 = {power(5)}")

# Exercise 4.4: Function with multiple return values
def min_max(numbers):
    return min(numbers), max(numbers)

numbers = [3, 7, 2, 9, 1, 5]
minimum, maximum = min_max(numbers)
print(f"\nMin: {minimum}, Max: {maximum}")

# Exercise 4.5: Lambda functions
square = lambda x: x ** 2
print(f"\n7 squared = {square(7)}")

# Exercise 4.6: Map, Filter, and Reduce
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(f"\nSquared numbers: {squared}")

numbers2 = [1, 2, 3, 4, 5, 6, 7, 8]
evens = list(filter(lambda x: x % 2 == 0, numbers2))
print(f"Even numbers: {evens}")

numbers3 = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers3)
print(f"Product: {product}")
