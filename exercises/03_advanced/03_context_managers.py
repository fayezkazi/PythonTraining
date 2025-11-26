"""
Exercise 9: Context Managers
=============================

Complete the following exercises to practice creating and using context managers.
"""

# Exercise 9.1: Using built-in context managers
# TODO: Use the 'with' statement to open and read a file


# Exercise 9.2: Basic context manager class
# TODO: Create a context manager class called 'Timer' that:
# - Records the start time in __enter__
# - Prints the elapsed time in __exit__


# TODO: Use the Timer context manager


# Exercise 9.3: Context manager with contextlib
# TODO: Import contextlib and create a context manager using the @contextmanager decorator
# that prints "Entering" when entering and "Exiting" when exiting


# TODO: Use the context manager


# Exercise 9.4: File handler context manager
# TODO: Create a context manager that opens a file for writing,
# writes some content, and ensures the file is closed


# Exercise 9.5: Database connection context manager
# TODO: Create a mock database context manager that:
# - Prints "Connecting to database" on enter
# - Prints "Closing connection" on exit
# - Handles exceptions gracefully
