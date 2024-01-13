from fractions import Fraction

# Input a fractional expression from the user
expression = input("Enter your Fractional expression: ")

# Split the expression into two fractions and the operator
fraction1, operator, fraction2 = map(str.strip, expression.split())

# Convert the fractions to Fraction objects
fraction1 = Fraction(fraction1)
fraction2 = Fraction(fraction2)

# Perform the operation based on the operator
if operator == '+':
    result = fraction1 + fraction2
elif operator == '-':
    result = fraction1 - fraction2
elif operator == '*':
    result = fraction1 * fraction2
else:
    print("Invalid operator. Please use '+', '-', or '*' for the operation.")
    exit()

# Print the result
print(f"The result = {result}")