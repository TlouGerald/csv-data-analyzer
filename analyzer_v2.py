"""
 CSV Sales Data Analyzer
 
 This program loads sales from a CSV file
 and provides different sales analysis
 features through an interactive menu.
"""

import csv

def load_data():
    required_columns = {"Product", "Category", "Quantity", "Price"}
    
    try:
        with open("sales_data.csv", "r") as file:
            reader = csv.DictReader(file)

            if reader.fieldnames is None:
                print("Error: CSV file has no header")
                return[]
            
            missing_columns = required_columns - set(reader.fieldnames)

            if missing_columns:
                print("Error: CSV is missing required columns:")
                print(", ".join(missing_columns))
                return

            data = list(reader)

        if not data:
            print("Error: sales_data.csv is empty.")
            return []

        for row_number, row in enumerate(data, start=2):
            if row["Product"].strip() == "" or row["Category"].strip() == "":
                print(
                    f"Error: Product or Category cannot be blank"
                    f"on row {row_number}."
                    )
                return []

            try:
                quantity = int(row["Quantity"])
                price = float(row["Price"])
            except ValueError:
                print(f"Error: Invalid numeric data for"
                      f"{row['Product']} on {row_number}.")
                return []

            if quantity <= 0 or price <= 0:
                print(f"Error: Quantity and Price must be greater than 0"
                      f"for {row['Product']} on {row_number}."
                      )
                return []
        
        return data

    except FileNotFoundError:
        print("Error: sales_data.csv was not found.")
        return[]

data = load_data()

def calculate_row_sales(row):
    quantity = int(row["Quantity"])
    price = float(row["Price"])
    sales = quantity * price

    return sales
    

def calculate_total_sales(data):
    total_sales = 0
    
    for row in data:
        sales = calculate_row_sales(row)
        total_sales = total_sales + sales
        
    return total_sales
    

def calculate_total_quantity(data):
    total_quantity_sold = 0

    for row in data:
        quantity = int(row["Quantity"])
        total_quantity_sold = total_quantity_sold + quantity

    return  total_quantity_sold

total_quantity_sold = calculate_total_quantity(data)


def find_best_product(data):
    highest_sales = 0
    best_product = ""

    for row in data:
        sales = calculate_row_sales(row)
        
        if sales > highest_sales:
            highest_sales = sales
            best_product = row["Product"]

    return best_product, highest_sales


def find_worst_product(data):
    lowest_sales = float("inf")
    worst_product = ""

    for row in data:
        sales = calculate_row_sales(row)

        if sales < lowest_sales:
            lowest_sales = sales
            worst_product = row["Product"]

    return worst_product, lowest_sales


def calculate_average_sale(data):
    total_sales = calculate_total_sales(data)
    product_count = 0
    average_sales = 0

    for row in data:
        product_count += 1

    average_sales = total_sales / product_count

    return average_sales


def calculate_sales_by_category(data):
    sales_by_category = {}

    for row in data:
         category = row["Category"]
         sales = calculate_row_sales(row)

         if category not in sales_by_category:
             sales_by_category[category] = 0

         sales_by_category[category] = sales_by_category[category] + sales

    return sales_by_category

sales_by_category = calculate_sales_by_category(data)
total_sales = calculate_total_sales(data)

def display_sales_by_category(data):
    print("\nSales by Category:")
    
    for category, sales in sales_by_category.items():
        percentage = (sales/total_sales  * 100)
        print(category, ":", sales, "-", round(percentage,2), "%")

def calculate_units_by_category(data):
    units_by_category = {}

    for row in data:
        category = row["Category"]
        quantity = int(row["Quantity"])

        if category not in units_by_category:
            units_by_category[category] = 0

        units_by_category[category] = units_by_category[category] + quantity

    return units_by_category

units_by_category = calculate_units_by_category(data)

def display_units_by_category(data):
    print("\nUnits by Category:")

    for category, quantity in units_by_category.items():
        percentage = (quantity / total_quantity_sold) * 100
        print(category, ":", quantity, "-", round(percentage, 2), "%")


def calculate_average_units_by_category(data):
    units_by_category = {}
    product_count = {}
    average_units = {}

    for row in data:
        category = row["Category"]
        quantity = int(row["Quantity"])
        product = row["Product"]

        if category not in units_by_category:
            units_by_category[category] = 0
            

        units_by_category[category] += quantity
        
        if category not in product_count:
            product_count[category] = 0
            
        product_count[category] +=1

    for category in units_by_category:
        average_units[category] = (units_by_category[category] / product_count[category])
    
    return average_units


def display_average_units_by_category(average_units):
    print("\nAverage Units Sold by Categgory")

    for category, average in average_units.items():
        print(category, ":", round(average, 2))
    
    
def display_product_performance(data):
    print("\nProduct Perfomance")
    print("-" * 80)
    products = []
        
    for row in data:
        product = row["Product"]
        category = row["Category"]
        quantity = int(row["Quantity"])
        price = float(row["Price"])
        
        sales = calculate_row_sales(row)

        product_info = {
            "Product": product,
            "Category": category,
            "Quantity": quantity,
            "Price": price,
            "Sales": sales
            }
        
        products.append(product_info)

    products = sorted(
        products,
        key = lambda product: product["Sales"],
        reverse = True
        )

    for product_info in products:
        print(
            f"{product_info['Product']} | "
            f"{product_info['Category']} | "
            f"Qauntity: {product_info['Quantity']} |"
            f"Price: R{product_info['Price']:,.2f} |"
            f"Sales: R{product_info['Sales']:,.2f}"
            )
        

def display_sales_summary(data):
    total_sales = calculate_total_sales(data)
    average_sales = calculate_average_sale(data)
    total_quantity = calculate_total_quantity(data)
    best_product, highest_sales = find_best_product(data)
    worst_product, lowest_sales = find_worst_product(data)
    
    print("\n======================================")
    print("       OVERALL SALES SUMMARY         ")
    print("======================================")
    print("Total Sales:", total_sales,
          "\nAverage Sales:", average_sales, 
          "\nTotal Units Sold:",total_quantity,
          "\nBest-selling Product:", best_product,
          "\nHighest Sales:", highest_sales ,
          "\nLowest-selling Product:", worst_product,
          "\nLowest Sales:", lowest_sales)


def display_menu():
    print("\n======================================")
    print("       CSV SALES DATA ANALYZER         ")
    print("======================================")
    print("1. View overall sales summary")
    print("2. View sales by category") 
    print("3. View best-selling product")
    print("4. View lowest-selling product")
    print("5. View product performance")
    print("6. View units by category")
    print("7. View average units by category") 
    print("8. Search for a product")
    print("9. Exit")


def search_product(data):
    product_name = input("Enter product name:")
    
    found = False

    for row in data:
        if row["Product"].lower() == product_name.lower():
            quantity = int(row["Quantity"])
            price = float(row["Price"])
            sales = calculate_row_sales(row)

            print("\nProduct found:")
            print("-" * 25)
            print("Product:", row["Product"])
            print("Category:", row["Category"])
            print("Quantity:", quantity)
            print(f"Price: R{price:,.2f}")
            print(f"Sales: R{sales:,.2f}")

            found = True
            break

    if not found:
        print("Product not found")
        

def main():
    
    if not data:
        return
    
    total_sales = calculate_total_sales(data)
    
    running = True

    while running:
        display_menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            display_sales_summary(data)
            input("\nPress enter to return to the menu...")

        elif choice == "2":
            sales_by_category = calculate_sales_by_category(data)
            display_sales_by_category(sales_by_category)
            input("\nPress enter to return to the menu...")
    
        elif choice == "3":
            best_product, highest_sales = find_best_product(data)
            print("Best-selling product:", best_product)
            print("Highest sales:", highest_sales)
            input("\nPress enter to return to the menu...")
    
        elif choice == "4":
            worst_product, lowest_sales = find_worst_product(data)
            print("Lowest-selling product:", worst_product)
            print("Lowest sales:", lowest_sales)
            input("\nPress enter to return to the menu...")

        elif choice == "5":
            display_product_performance(data)
            input("\nPress enter to return to the menu...")
            
        elif choice == "6":
            units_by_category = calculate_units_by_category(data)
            display_units_by_category(units_by_category)
            input("\nPress enter to return to the menu...")

        elif choice == "7":
            average_units = calculate_average_units_by_category(data)
            display_average_units_by_category(average_units)
            input("\nPress enter to return to the menu...")

        elif choice == "8":
            search_product(data)
            input("\nPress enter to return to the menu...")
            
    
        elif choice == "9":
            print("Thank you for using the CSV Sales Data Analyzer.")
            running = False

        else:
            print("Invalid choice. Please select a number from 1 to 9.")
            input("\nPress enter to return to the menu...")

if __name__ == "__main__":
    main()
