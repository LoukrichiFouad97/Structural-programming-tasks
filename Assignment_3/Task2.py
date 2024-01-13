celsius_temp = 100

while True:
    
    fahrenheit_temp = (celsius_temp * 9/5) + 32
    
    if int(celsius_temp) == int(fahrenheit_temp):
        break  
    else:
        celsius_temp -= 1 

print(f"The temp that is the same in both Celsius and Fahrenheit is: {int(celsius_temp)} degrees.")