"""
Module: jeje.py
Handles CSV file saving and loading operations.
"""

import csv

def save_csv(inventory, path, include_header=True):
    """
    Saves inventory to CSV file.
    """

    if not inventory:
        print("There are no products to save.")
        return

    try:
        with open(path, "w", newline="", encoding="utf-8") as file:

            writer = csv.writer(file)

            if include_header:
                writer.writerow(["name", "price", "quantity"])

            for product in inventory:
                writer.writerow([
                    product["name"],
                    product["price"],
                    product["quantity"]
                ])
        print(f"Inventory saved to: {path}")

    except PermissionError:
        print("Permission error while writing the file.")
    except Exception as error:
        print("Unexpected error while saving:", error)


def load_csv(path):
    """
    Loads products from CSV file.
    """

    inventory = []
    invalid_rows = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            header = next(reader)
            if header != ["name", "price", "quantity"]:
                print("Invalid header format.")
                return []
            
            for row in reader:
                if len(row) != 3:
                    invalid_rows += 1
                    continue

                try:
                    name = row[0]
                    price = float(row[1])
                    quantity = int(row[2])
                    if price < 0 or quantity < 0:
                        invalid_rows += 1
                        continue
                    product = {
                        "name": name,
                        "price": price,
                        "quantity": quantity
                    }
                    inventory.append(product)
                except ValueError:
                    invalid_rows += 1
        print("Products loaded:", len(inventory))
        print("Invalid rows skipped:", invalid_rows)

        return inventory

    except FileNotFoundError:
        print("File not found.")
        return []

    except UnicodeDecodeError:
        print("File encoding error.")
        return []

    except Exception as error:
        print("Unexpected error while loading:", error)
        return []