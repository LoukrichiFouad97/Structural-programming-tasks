class Pizza:
    DEEP_DISH = "Deep Dish"
    HAND_TOSSED = "Hand Tossed"
    PAN = "Pan"

    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"

    BASE_PRICES = {SMALL: 10, MEDIUM: 14, LARGE: 17}
    TOPPING_PRICE = 2

    def __init__(self, pizza_type, size, num_toppings):
        self.set_pizza(pizza_type, size, num_toppings)

    def set_pizza(self, pizza_type, size, num_toppings):
        if pizza_type not in [self.DEEP_DISH, self.HAND_TOSSED, self.PAN]:
            raise ValueError("Invalid pizza type.")
        if size not in [self.SMALL, self.MEDIUM, self.LARGE]:
            raise ValueError("Invalid pizza size.")
        if num_toppings < 0:
            raise ValueError("Number of toppings cannot be negative.")

        self.pizza_type = pizza_type
        self.size = size
        self.num_toppings = num_toppings

    def output_description(self):
        print(f"\nPizza Description:")
        print(f"Type: {self.pizza_type}")
        print(f"Size: {self.size}")
        print(f"Toppings: {self.num_toppings}")

    def compute_price(self):
        base_price = self.BASE_PRICES[self.size]
        topping_price = self.TOPPING_PRICE * self.num_toppings
        total_price = base_price + topping_price
        return total_price

def main():
    # Ask user for input data for one pizza
    pizza_type = input("Enter the type of pizza (Deep Dish, Hand Tossed, or Pan): ")
    size = input("Enter the size of pizza (Small, Medium, or Large): ")
    num_toppings = int(input("Enter the number of toppings: "))

    # Create a Pizza object with user-provided data
    pizza = Pizza(pizza_type, size, num_toppings)

    # Output description and price for the pizza
    pizza.output_description()
    print("Price:", pizza.compute_price())

if __name__ == "__main__":
    main()
