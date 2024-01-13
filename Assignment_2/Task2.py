
# Input height and weight from the user
height = float(input("Enter your height in centimeters: "))
weight = float(input("Enter your weight in kilograms: "))

# Calculate the thresholds for underweight, normal, and overweight
underweight_threshold = height / 2.5
normal_lower_threshold = height / 2.5
normal_upper_threshold = height / 2.3
overweight_threshold = height / 2.3

# Determine the category based on the criteria
if weight < underweight_threshold:
    print("You are underweight.")
elif normal_lower_threshold <= weight <= normal_upper_threshold:
    print("You have a normal weight.")
else:
    print("You are overweight.")
