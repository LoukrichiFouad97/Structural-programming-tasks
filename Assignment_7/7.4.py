class Temperature:
    def __init__(self, kelvin=0):
        self.set_temp_kelvin(kelvin)

    def set_temp_kelvin(self, kelvin):
        if not isinstance(kelvin, (int, float)):
            raise ValueError("Temperature must be a numeric value.")
        if kelvin < 0:
            raise ValueError("Temperature in Kelvin cannot be negative.")

        self._kelvin = kelvin

    def set_temp_fahrenheit(self, fahrenheit):
        celsius = (5 / 9) * (fahrenheit - 32)
        kelvin = celsius + 273.15
        self.set_temp_kelvin(kelvin)

    def set_temp_celsius(self, celsius):
        kelvin = celsius + 273.15
        self.set_temp_kelvin(kelvin)

    def get_temp_kelvin(self):
        return self._kelvin

    def get_temp_fahrenheit(self):
        celsius = self._kelvin - 273.15
        fahrenheit = (9 / 5) * celsius + 32
        return fahrenheit

    def get_temp_celsius(self):
        return self._kelvin - 273.15

def main():
    # Prompt the user for the number of temperature instances
    num_temps = int(input("Enter the number of temperature instances: "))

    # Collect temperature data for each instance
    temperature_instances = []
    for i in range(num_temps):
        kelvin = float(input(f"\nEnter temperature in Kelvin for Temperature {i + 1}: "))
        temp = Temperature(kelvin)
        temperature_instances.append(temp)

    # Display temperatures in all scales for each instance
    for i, temp in enumerate(temperature_instances):
        print(f"\nTemperature {i + 1}:")
        print(f"Kelvin: {temp.get_temp_kelvin()}K")
        print(f"Fahrenheit: {temp.get_temp_fahrenheit()}°F")
        print(f"Celsius: {temp.get_temp_celsius()}°C")

if __name__ == "__main__":
    main()
