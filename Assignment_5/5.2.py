# Constants for the number of salespeople and products
NUM_SALESPEOPLE = 4
NUM_PRODUCTS = 5
DAYS_IN_WEEK = 7

def main():
    # Initialize the sales array with random records for the past week
    sales = [[round(random.uniform(1000, 5000), 2) for _ in range(NUM_PRODUCTS)] for _ in range(NUM_SALESPEOPLE)]

    # Display the initial sales table
    print("Initial Sales Table:")
    display_sales_table(sales)

    # Read one daily information for all salespeople
    for salesperson in range(NUM_SALESPEOPLE):
        print(f"\nEnter sales information for salesperson {salesperson + 1} today:")
        for product in range(NUM_PRODUCTS):
            sales[salesperson][product] += float(input(f"Enter sales for product {product + 1}: "))

    # Display the updated sales table
    print("\nUpdated Sales Table:")
    display_sales_table(sales)

def display_sales_table(sales):
    # Display the header
    print("\nSalesperson   Product 1   Product 2   Product 3   Product 4   Product 5   Total")

    # Display the sales data
    for salesperson in range(NUM_SALESPEOPLE):
        print(f"{salesperson + 1:<13}", end="")
        total_salesperson = 0
        for product in range(NUM_PRODUCTS):
            print(f"${sales[salesperson][product]:<11.2f}", end="")
            total_salesperson += sales[salesperson][product]
        print(f"${total_salesperson:<11.2f}")

    # Display the column totals
    print("Total        ", end="")
    for product in range(NUM_PRODUCTS):
        total_product = sum(sales[salesperson][product] for salesperson in range(NUM_SALESPEOPLE))
        print(f"${total_product:<11.2f}", end="")

    # Display the grand total
    grand_total = sum(sum(sales[salesperson]) for salesperson in range(NUM_SALESPEOPLE))
    print(f"\nGrand Total  ${grand_total:.2f}")

if __name__ == "__main__":
    import random
    main()
