"""
Module: siwe2.py
Provides CRUD operations and statistical analysis for the inventory system.
"""


def add_product(inventory, name, price, quantity):
    """
    Adds a new product to the inventory.
    """

    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    inventory.append(product)
    print("Product successfully added.")


def show_inventory(inventory):
    """
    Displays all products in the inventory.
    """

    if not inventory:
        print("Inventory is empty.")
        return

    print("\nCurrent inventory:")

    for product in inventory:
        print(
            product["name"],
            "- Price:", product["price"],
            "- Quantity:", product["quantity"]
        )


def search_product(inventory, name):
    """
    Searches for a product by name.
    """

    for product in inventory:
        if product["name"].lower() == name.lower():
            return product

    return None


def update_product(inventory, name, new_price=None, new_quantity=None):
    """
    Updates product price or quantity.
    """

    product = search_product(inventory, name)

    if product:

        if new_price is not None:
            product["price"] = new_price

        if new_quantity is not None:
            product["quantity"] = new_quantity

        print("Product updated successfully.")

    else:
        print("Product not found.")


def delete_product(inventory, name):
    """
    Deletes a product from inventory.
    """

    product = search_product(inventory, name)

    if product:
        inventory.remove(product)
        print("Product removed successfully.")

    else:
        print("Product not found.")


def calculate_statistics(inventory):
    """
    Calculates inventory statistics.
    """

    if not inventory:
        return None

    total_units = sum(p["quantity"] for p in inventory)

    total_value = sum(
        p["price"] * p["quantity"]
        for p in inventory
    )

    most_expensive = max(
        inventory,
        key=lambda p: p["price"]
    )

    highest_stock = max(
        inventory,
        key=lambda p: p["quantity"]
    )

    return {
        "total_units": total_units,
        "total_value": total_value,
        "most_expensive": (
            most_expensive["name"],
            most_expensive["price"]
        ),
        "highest_stock": (
            highest_stock["name"],
            highest_stock["quantity"]
        )
    }