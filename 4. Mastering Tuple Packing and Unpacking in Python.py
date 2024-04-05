
'''
Task 1: Customer Order Processing
Refine your skills in tuple unpacking by managing customer orders.

Problem Statement:
You are given a list of tuples, each representing a customer's order. Each tuple contains the customer's name, 
the product ordered, and the quantity. Your task is to unpack each tuple and print the order details in a user-friendly format.

Sample Order Data:

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    # More orders...
]
Write a function to iterate over the list of orders.
Unpack each tuple in the list and format the details for display.
'''

def process_orders(orders):
    for i, order in enumerate(orders, start=1):
        customer_name, product, quantity = order
        print(f"Order {i}: Customer {customer_name} ordered {quantity} {product}(s).")

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Charlie", "Smartphone", 3)
]

process_orders(orders)

'''
Task 2: Sorting and Filtering Contact Information
Implement tuple packing and unpacking in sorting and filtering tasks.

Problem Statement:
You have a list of contacts, where each contact is represented as a tuple containing a name, email, and phone number. 
Your task is to:

Sort the contacts by name.
Filter and display contacts whose names start with a specific letter.
Sample Contact Data:

contacts = [
    ("Alice", "alice@email.com", "123-456-7890"),
    ("Bob", "bob@email.com", "234-567-8901"),
    # More contacts...
]
'''

def sort_and_filter_contacts(contacts, start_letter):
    sorted_contacts = sorted(contacts, key=lambda x: x[0])
    
    print("Sorted contacts:")
    for name, email, phone in sorted_contacts:
        print(f"Name: {name}, Email: {email}, Phone: {phone}")

    filtered_contacts = [contact for contact in contacts if contact[0].startswith(start_letter)]
    
    print(f"\nContacts whose names start with '{start_letter}':")
    for name, email, phone in filtered_contacts:
        print(f"Name: {name}, Email: {email}, Phone: {phone}")

contacts = [
    ("Alice", "alice@email.com", "123-456-7890"),
    ("Bob", "bob@email.com", "234-567-8901"),
    ("Charlie", "charlie@email.com", "345-678-9012")
]

sort_and_filter_contacts(contacts, 'B')