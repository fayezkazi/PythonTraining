"""
Solution 6: File I/O and Exception Handling
===========================================
"""

import os
import csv

# Exercise 6.1: Writing to a file
def write_file():
    with open('sample.txt', 'w') as f:
        f.write("First line\n")
        f.write("Second line\n")
        f.write("Third line\n")
    print("File written successfully")

write_file()

# Exercise 6.2: Reading from a file
def read_file():
    with open('sample.txt', 'r') as f:
        content = f.read()
        print("\nFile contents:")
        print(content)

read_file()

# Exercise 6.3: Exception handling
def safe_divide(a, b):
    try:
        result = a / b
        print(f"\n{a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        print("\nError: Cannot divide by zero!")
        return None

safe_divide(10, 2)
safe_divide(10, 0)

# Exercise 6.4: Try/Except/Finally
def read_file_safe(filename):
    f = None
    try:
        f = open(filename, 'r')
        content = f.read()
        print(f"\nRead {len(content)} characters from {filename}")
        return content
    except FileNotFoundError:
        print(f"\nError: File {filename} not found")
        return None
    finally:
        if f:
            f.close()
            print("File closed")

read_file_safe('sample.txt')

# Exercise 6.5: Context managers
def read_with_context():
    with open('sample.txt', 'r') as f:
        lines = f.readlines()
        print(f"\nRead {len(lines)} lines using context manager")

read_with_context()

# Exercise 6.6: Working with CSV files
def write_csv():
    with open('people.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['name', 'age', 'city'])
        writer.writerow(['Alice', 25, 'New York'])
        writer.writerow(['Bob', 30, 'San Francisco'])
        writer.writerow(['Charlie', 35, 'Chicago'])
    print("\nCSV file created")

def read_csv():
    with open('people.csv', 'r') as f:
        reader = csv.reader(f)
        print("\nCSV contents:")
        for row in reader:
            print(', '.join(row))

write_csv()
read_csv()

# Clean up
if os.path.exists('sample.txt'):
    os.remove('sample.txt')
if os.path.exists('people.csv'):
    os.remove('people.csv')
print("\nCleanup complete")
