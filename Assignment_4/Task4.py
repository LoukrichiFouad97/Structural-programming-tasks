def get_user_input():
    height = float(input("Enter your height in centimeters: "))
    weight = float(input("Enter your weight in kilograms: "))
    return height, weight

def calculate_bmi(height, weight):
    bmi = weight / ((height / 100) ** 2)
    return bmi

def determine_weight_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal"
    else:
        return "Overweight"

def display_result(height, weight, bmi, category):
    print(f"\nHeight: {height} cm\nWeight: {weight} kg\nBMI: {bmi:.2f}\nCategory: {category}\n")

def main():
    height, weight = get_user_input()
    bmi = calculate_bmi(height, weight)
    category = determine_weight_category(bmi)
    display_result(height, weight, bmi, category)

if __name__ == "__main__":
    main()
