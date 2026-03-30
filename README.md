# Inventory Management System (Python)

## Overview

The **Inventory Management System** is a modular Python console application designed to manage products using standard business operations.
It supports **CRUD operations**, **statistical analysis**, and **data persistence using CSV files**, ensuring that inventory data can be stored and reused across sessions.

This project demonstrates core software engineering practices such as:

* Modular programming
* Data validation
* Exception handling
* File persistence
* Business logic separation
* Clean and maintainable code structure

The system is suitable for educational purposes and as a foundation for real-world inventory applications.

---

## Features

* Add new products to the inventory
* Display all stored products
* Search products by name
* Update product price and quantity
* Delete products from inventory
* Calculate inventory statistics
* Save inventory data to CSV files
* Load inventory data from CSV files
* Merge or overwrite inventory data
* Input validation and error handling
* Continuous execution using a main loop

---

## Project Structure

```
inventory_system/
│
├── siwe.py      # Main program (menu and control flow)
├── siwe2.py     # Business logic (CRUD operations and statistics)
├── jeje.py      # File persistence (CSV handling)
└── README.md    # Project documentation
```

---

## Data Model

The inventory is stored in memory as a **list of dictionaries**, where each product follows this structure:

```python
{
    "name": str,
    "price": float,
    "quantity": int
}
```

---

## Requirements

* Python **3.8** or higher
* Standard Python libraries only:

  * `csv`

No external dependencies are required.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/inventory-system.git
```

2. Navigate to the project directory:

```bash
cd inventory-system
```

3. Run the application:

```bash
python siwe.py
```

---

## Usage

When the program starts, the user will see the main menu:

```
--- INVENTORY SYSTEM ---

1. Add product
2. Show inventory
3. Search product
4. Update product
5. Delete product
6. Statistics
7. Save CSV
8. Load CSV
9. Exit
```

The program will continue running until the user selects:

```
9. Exit
```

---

## Statistics Calculated

The system computes the following business metrics:

* **Total units**
  Sum of all product quantities

* **Total value**
  Sum of:

```
price × quantity
```

* **Most expensive product**
  Product with the highest price

* **Highest stock product**
  Product with the largest quantity

---

## CSV File Format

The system uses a standard CSV structure:

```
name,price,quantity
Laptop,1500.0,10
Mouse,25.5,50
Keyboard,45.0,30
```

Rules:

* The file must contain a header
* Each row must have exactly 3 columns
* Price must be a float
* Quantity must be an integer
* Negative values are not allowed

Invalid rows are skipped and reported.

---

## Error Handling

The system safely handles common runtime errors, including:

* Invalid numeric input
* Missing files
* Permission errors
* Invalid CSV format
* Encoding errors
* Unexpected exceptions

The application will never terminate unexpectedly due to user input errors.

---

## Business Logic Modules

### siwe2.py

Handles:

* Product management (CRUD)
* Inventory statistics
* Search operations

### jeje.py

Handles:

* CSV file saving
* CSV file loading
* Data validation
* Error reporting

### siwe.py

Handles:

* User interface
* Menu navigation
* Program lifecycle

---

## Future Improvements

Possible enhancements for production-level systems:

* Persistent database integration (SQLite / PostgreSQL)
* User authentication
* Logging system
* Inventory categories
* Product IDs
* REST API integration
* Graphical user interface (GUI)
* Automatic backups
* Unit testing

---

## Author

Alejo Z

Student Project — Inventory Management System
Python Modular Programming and File Persistence

---

## License

This project is for educational purposes.
