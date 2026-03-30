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

## Project Structure

```
inventory_system/
│
├── siwe.py      # Main program (menu and control flow)
├── siwe2.py     # Business logic (CRUD operations and statistics)
├── jeje.py      # File persistence (CSV handling)
└── README.md    # Project documentation
```

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
-Alejandro Gonzalez
-Inventory Management System
---
