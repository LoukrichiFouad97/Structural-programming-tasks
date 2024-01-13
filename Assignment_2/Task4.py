
# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Input choice from the user
choice = input("Please Enter (C) for Celsius and (F) for Fahrenheit: ")

# Validate user choice
if choice.upper() not in ['C', 'F']:
    print("Invalid choice. Please enter 'C' or 'F'.")
else:
    # Input temperature value
    temperature_value = float(input("Enter the temperature value: "))

    # Perform conversion based on user choice
    if choice.upper() == 'C':
        # Convert Celsius to Fahrenheit
        result = celsius_to_fahrenheit(temperature_value)
        print(f"The temperature is {result:.2f} Fahrenheit.")
    else:
        # Convert Fahrenheit to Celsius
        result = fahrenheit_to_celsius(temperature_value)
        print(f"The temperature is {result:.2f} Celsius.")