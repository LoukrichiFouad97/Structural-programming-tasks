def main():
    # Define the months and their corresponding average rainfall
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    average_rainfall = [3.2, 3.4, 3.6, 3.0, 2.8, 2.6, 2.4, 2.3, 2.5, 2.7, 3.0, 3.2]

    # Get the current month
    current_month = input("Enter the current month: ")

    # Get the actual rainfall for the previous 12 months
    actual_rainfall = []
    for i in range(11, -1, -1):
        month = months[(months.index(current_month) - i) % 12]
        rainfall = float(input(f"Enter the rainfall for {month}: "))
        actual_rainfall.append(rainfall)

    # Print the formatted table
    print("\nMonthly Rainfall Report:")
    print(f"\n{'Month':<10}{'Actual':<10}{'Average':<10}{'Diff':<10}")
    print("-" * 40)

    for i in range(12):
        diff = actual_rainfall[i] - average_rainfall[i]
        print(f"{months[i]:<10}{actual_rainfall[i]:<10.1f}{average_rainfall[i]:<10.1f}{diff:<10.1f}")

    # Print the bar graph
    print("\nRainfall Bar Graph:")
    for i in range(12):
        print(f"{months[i]}: {'*' * int(actual_rainfall[i])}")

if __name__ == "__main__":
    main()
