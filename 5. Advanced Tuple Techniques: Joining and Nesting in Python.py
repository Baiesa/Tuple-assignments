'''
Objective:
This assignment is designed to advance your understanding and application of joining and nesting tuples in Python. You will engage in tasks that require organizing and manipulating complex data structures, improving your problem-solving skills in handling multi-dimensional data.

Task 1: Product Catalog Merging
Utilize tuple joining to combine multiple product catalogs.

Problem Statement:
You are managing the product catalogs for an online store. Each catalog is a tuple of products, and each product is a tuple containing the product name and price. Merge multiple catalogs into a single tuple.

Write a function to join two or more product catalogs into one.
Display the combined catalog, ensuring that it maintains the order of products as they were in their original catalogs.
Example Catalogs:

catalog1 = (("Laptop", 1000), ("Camera", 500))
catalog2 = (("Smartphone", 800), ("Tablet", 450))
'''

def merge_product_catalogs(*catalogs):
    merged_catalog = ()
    for catalog in catalogs:
        merged_catalog += catalog
    return merged_catalog

catalog1 = (("Laptop", 1000), ("Camera", 500))
catalog2 = (("Smartphone", 800), ("Tablet", 450))


combined_catalog = merge_product_catalogs(catalog1, catalog2)

print("Combined Catalog:")
for product in combined_catalog:
    print(f"Product: {product[0]}, Price: {product[1]}")