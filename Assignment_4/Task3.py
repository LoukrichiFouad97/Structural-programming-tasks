def get_weight_input():
    pounds = float(input("Enter weight in pounds: "))
    ounces = float(input("Enter weight in ounces: "))
    return pounds, ounces

def calculate_weight(pounds, ounces):
    total_pounds = pounds + ounces / 16.0
    kilograms = total_pounds / 2.2046
    grams = kilograms * 1000
    return kilograms, grams

def display_output(pounds, ounces, kilograms, grams):
    print(f"\nWeight: {pounds:.2f} pounds {ounces:.2f} ounces")
    print(f"Equivalent: {kilograms:.2f} kilograms {grams:.2f} grams\n")

def main():
    while True:
        pounds, ounces = get_weight_input()
        kilograms, grams = calculate_weight(pounds, ounces)
        display_output(pounds, ounces, kilograms, grams)

        repeat = input("Do you want to calculate again? (yes/no): ").lower()
        if repeat != 'yes':
            break

if __name__ == "__main__":
    main()
