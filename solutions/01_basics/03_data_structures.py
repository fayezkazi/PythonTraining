"""
Solution 3: Data Structures (Lists, Tuples, Dictionaries, Sets)
===============================================================
"""

# Exercise 3.1: Lists
fruits = ["apple", "banana", "orange", "mango", "grape"]
print(f"Original fruits: {fruits}")

fruits.append("strawberry")
print(f"After adding strawberry: {fruits}")

fruits.pop(0)
print(f"After removing first fruit: {fruits}")

print(f"Length of list: {len(fruits)}")
print(f"Fruit at index 2: {fruits[2]}")

# Exercise 3.2: Tuples
colors = ("red", "green", "blue")
print(f"\nColors tuple: {colors}")
print(f"First color: {colors[0]}")

# Uncommenting the following line would cause an error
# colors[0] = "yellow"  # TypeError: 'tuple' object does not support item assignment

# Exercise 3.3: Dictionaries
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(f"\nPerson dictionary: {person}")

person["occupation"] = "Engineer"
print(f"After adding occupation: {person}")

print(f"Person's name: {person['name']}")
print(f"Dictionary keys: {person.keys()}")
print(f"Dictionary values: {person.values()}")

# Exercise 3.4: Sets
numbers = {1, 2, 3, 4, 5}
print(f"\nNumbers set: {numbers}")

numbers.add(3)  # Won't add duplicate
print(f"After trying to add duplicate 3: {numbers}")
print(f"Length of set: {len(numbers)}")

# Exercise 3.5: List comprehension
squares = [x ** 2 for x in range(1, 11)]
print(f"\nSquares: {squares}")

evens = [x for x in range(1, 21) if x % 2 == 0]
print(f"Even numbers: {evens}")
