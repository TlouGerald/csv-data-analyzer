# CSV Data Analyzer

A Python-based command-line application that loads and analyzes sales data from a CSV file.

## Features

- Load sales data from a CSV file
- Validate CSV structure and data
- Calculate total sales
- Calculate average sales
- Identify the best-selling product
- Identify the lowest-selling product
- Display sales by category
- Display units sold by category
- Calculate average units sold by category
- Display product performance rankings
- Search for individual products
- Handle invalid or missing data safely
- Interactive menu-driven interface

## Technologies Used

- Python
- CSV
- Dictionaries
- Functions
- Loops
- Exception handling
- Data validation

## Dataset

The project uses a sample sales dataset containing:

- Product
- Category
- Quantity
- Price

## Example Analysis

The program can produce results such as:

- Total Sales: R231,850.00
- Average Sale: R23,185.00
- Total Units Sold: 97

It can also break sales and units down by category and rank products based on total sales.

## How to Run

1. Make sure Python is installed.
2. Download or clone this repository.
3. Make sure `sales_data.csv` is in the same folder as `analyzer_v2.py`.
4. Run:

```bash
python analyzer_v2.py```

5. Select an option from the menu.

## Key Learning Outcomes

Through this project, I practiced:
- Reading and processing CSV data
- Working with dictionaries and lists
- Creating reusable functions
- Using loops and conditional statements
- Handling exceptions
- Validating input data
- Building a menu-driven Python application
- Structuring a Python project
- Thinking about real-world data quality issues

## Future Improvements

Possible future improvements include:
- Adding graphical data visualizations
- Using Pandas for larger datasets
- Exporting analysis results
- Adding automated tests
- Supporting multiple CSV files
