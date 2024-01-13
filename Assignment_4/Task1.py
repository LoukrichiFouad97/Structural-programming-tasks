def calculate_wind_chill_index(wind_speed, temperature):
    """
    Calculate the wind chill index.

    Parameters:
    - wind_speed: Wind speed in m/sec
    - temperature: Temperature in degrees Celsius (should be <= 10)

    Returns:
    - Wind chill index in degrees Celsius
    """

    if temperature >= 10:
        raise ValueError("Temperature should be 10 degrees Celsius or lower.")

    # Calculate wind chill index
    wind_chill_index = 13.12 + 0.6215 * temperature - 11.37 * (wind_speed ** 0.16) + 0.3965 * temperature * (wind_speed ** 0.16)

    return wind_chill_index


wind_speed = float(input("Enter the wind speed: "))
temperature = float(input("enter the temperature in Celcius: "))

try:
    result = calculate_wind_chill_index(wind_speed, temperature)
    print(f"The wind chill index is: {result:.2f} degrees Celsius")
except ValueError as e:
    print(f"Error: {e}")
