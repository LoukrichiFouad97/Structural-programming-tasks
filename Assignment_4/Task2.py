def calculate_charges(hours_parked):
    # Minimum fee for up to three hours
    minimum_fee = 2.00
    
    # Additional charge per hour after the first three hours
    hourly_rate = 0.50
    
    # Maximum charge for any given 24-hour period
    maximum_charge = 10.00
    
    # Calculate the charge for the given hours
    if hours_parked <= 3:
        return minimum_fee
    elif hours_parked <= 24:
        return min(minimum_fee + (hours_parked - 3) * hourly_rate, maximum_charge)
    else:
        return maximum_charge

def main():
    total_receipts = 0.0

    # Number of customers (you can replace this with actual data input)
    num_customers = int(input("Enter the number of customers: "))

    for customer in range(1, num_customers + 1):
        hours = float(input(f"Enter hours parked for customer {customer}: "))
        charge = calculate_charges(hours)
        total_receipts += charge

        print(f"Customer {customer}: Charge ${charge:.2f}")

    print(f"\nTotal receipts for yesterday: ${total_receipts:.2f}")

if __name__ == "__main__":
    main()
