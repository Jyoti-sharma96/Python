# Bookstore Inventory and Analytics System

A robust Python-based application built with **Pandas** and **NumPy** for managing bookstore inventory, tracking sales transactions, and generating comprehensive business intelligence reports and visualizations.

---

## 📌 Features

- **Inventory Management**: Add new books, update stock quantities, and track book details (Title, Author, Genre, Price, Quantity).
- **Sales Tracking**: Record sales transactions with automatic inventory deduction and revenue calculation.
- **Data Analytics**: Compute key business metrics using NumPy (total revenue, average book price, monthly revenue growth rates).
- **Aggregations & Insights**: Analyze top-performing books, revenue breakdown by genre, and author performance.
- **Data Visualization**: Generate professional charts using Seaborn and Matplotlib (e.g., Sales by Genre).

---

## 📁 Project Structure

```text
├── inventory.csv       # Bookstore inventory dataset
├── sales.csv           # Sales transactions dataset
├── main.ipynb          # Jupyter Notebook containing the implementation
└── README.md           # Project documentation
```

---

## 📊 Dataset Schemas

### 1. `inventory.csv`
| Column | Data Type | Description |
| :--- | :--- | :--- |
| `Title` | String | The title of the book |
| `Author` | String | The author of the book |
| `Genre` | String | Literary genre (Fiction, Dystopian, Sci-Fi, etc.) |
| `Price` | Float | Unit price in USD ($) |
| `Quantity` | Integer | Current available stock in inventory |

### 2. `sales.csv`
| Column | Data Type | Description |
| :--- | :--- | :--- |
| `Date` | Date (YYYY-MM-DD) | Date of the sales transaction |
| `Title` | String | The title of the book sold |
| `Quantity Sold` | Integer | Number of units sold in the transaction |
| `Total Revenue` | Float | Total revenue generated ($) |

---

## 🚀 Getting Started

### Prerequisites
Make sure you have Python 3.8+ installed along with the required data science libraries:

```bash
pip install pandas numpy matplotlib seaborn
```

### Quick Start Code

Initialize the bookstore system and perform inventory and sales operations directly in Python or Jupyter Notebook:

```python
import pandas as pd
import numpy as np
from bookstore import Bookstore  # or run within the notebook context

# Initialize bookstore system
store = Bookstore()

# Add a new book to inventory
store.add_book("Dune", "Frank Herbert", "Sci-Fi", 16.50, 40)

# Update existing stock quantity
store.update_inventory("1984", 10)

# Record a sale transaction
store.record_sale("Dune", 5, "2026-07-01")

# Generate summary report
store.generate_report()
```

---

## 📈 Analytics & Metrics

The system calculates advanced financial and inventory metrics:
- **Total Revenue**: Accumulated sales revenue across all transactions.
- **Average Book Price**: Mean price across all catalog titles.
- **Monthly Revenue Growth Rate**: Month-over-month percentage change in revenue computed via NumPy arrays (`np.diff`).

---

## 🛠️ Core Class Reference (`Bookstore`)

- `__init__(inventory_file, sales_file)`: Initializes datasets.
- `add_book(title, author, genre, price, quantity)`: Inserts a new title with validation.
- `update_inventory(title, quantity)`: Adjusts existing stock levels.
- `record_sale(title, quantity, date)`: Deducts stock and logs transaction revenue.
- `generate_report()`: Prints high-level summary statistics.

---

## 📄 License
This project is open-source and available for educational and commercial use.
