"""
Solution 9: Context Managers
=============================
"""

import time
from contextlib import contextmanager

# Exercise 9.1: Using built-in context managers
# Create a sample file first
with open('test.txt', 'w') as f:
    f.write("This is a test file")

print("Reading file using context manager:")
with open('test.txt', 'r') as f:
    content = f.read()
    print(content)

# Exercise 9.2: Basic context manager class
class Timer:
    def __enter__(self):
        self.start = time.time()
        print("\nTimer started")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        elapsed = end - self.start
        print(f"Timer stopped. Elapsed time: {elapsed:.4f} seconds")
        return False

print("\nUsing Timer context manager:")
with Timer():
    time.sleep(0.5)
    print("Doing some work...")

# Exercise 9.3: Context manager with contextlib
@contextmanager
def my_context():
    print("\nEntering")
    try:
        yield
    finally:
        print("Exiting")

print("\nUsing contextlib decorator:")
with my_context():
    print("Inside context")

# Exercise 9.4: File handler context manager
class FileHandler:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        return False

print("\nUsing FileHandler context manager:")
with FileHandler('output.txt', 'w') as f:
    f.write("Writing with custom context manager\n")
print("File written and closed")

# Exercise 9.5: Database connection context manager
class DatabaseConnection:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connection = None
    
    def __enter__(self):
        print(f"\nConnecting to database: {self.connection_string}")
        self.connection = "MockConnection"
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing connection")
        if exc_type is not None:
            print(f"Exception occurred: {exc_val}")
        return False

print("\nUsing DatabaseConnection context manager:")
with DatabaseConnection("localhost:5432/mydb") as conn:
    print(f"Using connection: {conn}")
    print("Executing queries...")

# Cleanup
import os
if os.path.exists('test.txt'):
    os.remove('test.txt')
if os.path.exists('output.txt'):
    os.remove('output.txt')
print("\nCleanup complete")
