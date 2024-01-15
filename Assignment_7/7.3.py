class Money:
    def __init__(self, dollars=0, cents=0):
        self.set_money(dollars, cents)

    def set_money(self, dollars, cents):
        if not isinstance(dollars, int) or not isinstance(cents, int):
            raise ValueError("Dollars and cents must be integers.")
        if cents < 0 or cents >= 100:
            raise ValueError("Cents must be between 0 and 99.")

        self._dollars = dollars
        self._cents = cents

    def get_dollars(self):
        return self._dollars

    def get_cents(self):
        return self._cents

    def get_amount(self):
        return float(f"{self._dollars}.{self._cents:02d}")

def main():
    # Prompt the user for values for two Money objects
    dollars1 = int(input("Enter dollars for Money 1: "))
    cents1 = int(input("Enter cents for Money 1: "))
    money1 = Money(dollars1, cents1)

    dollars2 = int(input("\nEnter dollars for Money 2: "))
    cents2 = int(input("Enter cents for Money 2: "))
    money2 = Money(dollars2, cents2)

    # Display the values using accessor functions
    print("\nMoney 1:")
    print(f"Dollars: {money1.get_dollars()}, Cents: {money1.get_cents()}")
    print("Amount:", money1.get_amount())

    print("\nMoney 2:")
    print(f"Dollars: {money2.get_dollars()}, Cents: {money2.get_cents()}")
    print("Amount:", money2.get_amount())

    # Test mutator function
    new_dollars1 = int(input("\nEnter new dollars for Money 1: "))
    new_cents1 = int(input("Enter new cents for Money 1: "))
    money1.set_money(new_dollars1, new_cents1)

    print("\nUpdated Money 1:")
    print(f"Dollars: {money1.get_dollars()}, Cents: {money1.get_cents()}")
    print("Amount:", money1.get_amount())

if __name__ == "__main__":
    main()
