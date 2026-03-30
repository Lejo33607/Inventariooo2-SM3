"""
Main file: siwe.py
Controls the program flow and user interaction.
"""

from siwe2 import *
from jeje import *


def menu():

    inventory = []

    while True:
        print("\n--- INVENTORY SYSTEM --- \n1. Add product \n2. Show inventory \n3. Search product \n4. Update product \n5. Delete product \n6. Statistics \n7. Save CSV \n8. Load CSV \n9. Exit")
        try:
            option = int(input("Select an option: \n>> "))

            if option == 1:
                name = input("Product name: \n>> ")
                price = float(input("Price: \n>> "))
                quantity = int(input("Quantity: \n>> "))
                
                add_product(
                    inventory,
                    name,
                    price,
                    quantity
                )
                
            elif option == 2:
                show_inventory(inventory)

            elif option == 3:
                name = input("Enter product name: \n>> ")
                
                product = search_product(
                    inventory,
                    name
                )

                if product:
                    print(product)
                else:
                    print("Product not found.")

            elif option == 4:

                name = input("Product name: \n>> ")
                price = float(input("New price: \n>> "))
                quantity = int(input("New quantity: \n>> "))

                update_product(
                    inventory,
                    name,
                    price,
                    quantity
                )

            elif option == 5:
                name = input("Product name to delete: \n>> ")

                delete_product(
                    inventory,
                    name
                )

            elif option == 6:
                stats = calculate_statistics(
                    inventory
                )

                if stats:
                    print("\nStatistics:")
                    print(
                        "Total units:",
                        stats["total_units"]
                    )
                    print(
                        "Total value:",
                        stats["total_value"]
                    )
                    print(
                        "Most expensive product:",
                        stats["most_expensive"]
                    )
                    print(
                        "Highest stock product:",
                        stats["highest_stock"]
                    )
                else:
                    print("Inventory is empty.")

            elif option == 7:
                path = input("Enter file path: \n>> ")

                save_csv(
                    inventory,
                    path
                )

            elif option == 8:
                path = input("Enter file path: \n>> ")

                new_inventory = load_csv(
                    path
                )

                if new_inventory:
                    decision = input(
                        "Overwrite current inventory? (Y/N): "
                    )
                    if decision.upper() == "Y":
                        inventory = new_inventory
                    else:
                        inventory.extend(new_inventory)

            elif option == 9:
                print("Exiting program...")
                break
            else:
                print("Invalid option.")

        except ValueError:
            print(
                "Invalid input. Please enter numeric values."
            )

if __name__ == "__main__":
    menu()