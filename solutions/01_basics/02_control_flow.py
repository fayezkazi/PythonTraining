"""
Solution 2: Control Flow (if/elif/else, loops)
==============================================
"""

# Exercise 2.1: If/Else statements
number = -5
if number > 0:
    print(f"{number} is positive")
elif number < 0:
    print(f"{number} is negative")
else:
    print("The number is zero")

# Exercise 2.2: For loops
print("\nNumbers from 1 to 10:")
for i in range(1, 11):
    print(i, end=" ")
print()

# Exercise 2.3: While loops
print("\nEven numbers from 0 to 20:")
count = 0
while count <= 20:
    print(count, end=" ")
    count += 2
print()

# Exercise 2.4: Nested loops
print("\nMultiplication table:")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i * j:3}", end=" ")
    print()

# Exercise 2.5: Loop with break and continue
print("\nNumbers with skip and break:")
for i in range(1, 11):
    if i == 5:
        continue
    if i == 9:
        break
    print(i, end=" ")
print()

# Exercise 2.6: FizzBuzz
print("\nFizzBuzz:")
for i in range(1, 31):
    if i % 15 == 0:
        print("FizzBuzz", end=" ")
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")
print()
