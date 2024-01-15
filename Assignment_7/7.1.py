class Fraction:
    def __init__(self, numerator=0, denominator=1):
        self.set_fraction(numerator, denominator)

    def set_fraction(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        self.numerator = numerator
        self.denominator = denominator
        self.reduce_fraction()

    def reduce_fraction(self):
        gcd = self.find_gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    def find_gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def get_value(self):
        return self.numerator / self.denominator

    def display_fraction(self):
        print(f"{self.numerator}/{self.denominator}")

def main():
    # Create a Fraction object and test the functionality
    fraction = Fraction()

    numerator_input = int(input("Enter the numerator: "))
    denominator_input = int(input("Enter the denominator: "))

    try:
        fraction.set_fraction(numerator_input, denominator_input)
        print("\nFraction as a double:", fraction.get_value())
        print("Reduced Fraction:")
        fraction.display_fraction()

    except ValueError as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main()
