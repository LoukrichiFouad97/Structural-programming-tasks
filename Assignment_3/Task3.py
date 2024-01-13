numbers = []

for i in range(5):
    num = int(input(f"Enter number {i + 1} between 1 and 30: "))
    numbers.append(num)

# Calculate the average of the entered numbers
average = sum(numbers) / len(numbers)

for num in numbers:
    print('*' * num)

print(f"\nAverage: {average}")
