
'''
Objective:
This assignment is designed to enhance your understanding and application of Python's core data structures - tuples, lists, and dictionaries - in real-world contexts. By engaging with these tasks, you will practice manipulating these data structures, applying built-in Python methods, and implementing error handling in practical situations.

Task 1: Library System Enhancement
Sharpen your skills in managing and modifying data within tuples and lists.

Problem Statement:
You are maintaining a library system where each book is stored as a tuple within a list. Your task is to update this system by adding new books and ensuring no duplicates.

Existing Library Data:

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
Add functionality to insert new books into library.
Ensure that adding a duplicate book is handled appropriately.
'''
def add_book(library, book):
    if book in library:
        print("This book already exists in the library.")
    else:
        library.append(book)
        print("Book added successfully.")

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

add_book(library, ("Animal Farm", "George Orwell",))  # Duplicate book
add_book(library, ("To Kill a Mockingbird", "Harper Lee"))  # New book

print("Updated library:", library)