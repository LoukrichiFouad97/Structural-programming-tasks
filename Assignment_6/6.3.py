def calculate_salary(gross_sales):
    base_salary = 200
    commission_rate = 0.09
    total_salary = base_salary + (commission_rate * gross_sales)
    return int(total_salary)

def count_salespeople_in_ranges(salaries):
    salary_ranges = [0] * 9  # Initialize counters for each specified salary range

    for salary in salaries:
        for i in range(len(salary_ranges)):
            lower_bound = 200 + i * 100
            upper_bound = lower_bound + 99

            if lower_bound <= salary <= upper_bound:
                salary_ranges[i] += 1
                break
        else:
            salary_ranges[-1] += 1  # If the salary is over $1000

    return salary_ranges

def display_commission_list(gross_sales, salaries):
    print("\nCommission List:")
    print("Salesperson   Gross Sales   Salary")
    for i in range(len(gross_sales)):
        print(f"{i + 1:<14}{gross_sales[i]:<14.2f}${salaries[i]:.2f}")

def main():
    num_salespeople = int(input("Enter the number of salespeople: "))

    # Input gross sales for each salesperson
    gross_sales = [float(input(f"Enter gross sales for salesperson {i + 1}: ")) for i in range(num_salespeople)]

    # Calculate salaries and store them in a dynamic array of doubles
    salaries = [calculate_salary(sales) for sales in gross_sales]

    # Use an integer array of counters to hold the summary of salary ranges
    salary_ranges = count_salespeople_in_ranges(salaries)

    # Display the detailed commission list
    display_commission_list(gross_sales, salaries)

    # Display the summary of specified salary ranges
    print("\nSummary of Salary Ranges:")
    for i in range(len(salary_ranges)):
        lower_bound = 200 + i * 100
        upper_bound = lower_bound + 99
        if i < len(salary_ranges) - 1:
            print(f"${lower_bound}-{upper_bound}: {salary_ranges[i]} salespeople")
        else:
            print(f"${lower_bound} and over: {salary_ranges[i]} salespeople")

if __name__ == "__main__":
    main()
