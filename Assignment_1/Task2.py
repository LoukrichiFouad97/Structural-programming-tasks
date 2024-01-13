# Constants
pounds_per_kilogram = 2.2
calories_per_minute_factor = 0.0175

# Input the subject's weight in pounds
weight_in_pounds = float(input("Enter the subject's weight in pounds: "))

# Input the MET value for the activity
mets = float(input("Enter the MET value for the activity: "))

# Input the number of minutes spent in the activity
minutes = float(input("Enter the number of minutes spent in the activity: "))

# Convert weight to kilograms
weight_in_kilograms = weight_in_pounds / pounds_per_kilogram

# Calculate the total number of calories burned
calories_burned = calories_per_minute_factor * mets * weight_in_kilograms * minutes

# Print the result
print(f"The estimated total number of calories burned is: {calories_burned:.2f} calories.")