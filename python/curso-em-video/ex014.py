# Python Exercise 14: Write a program that reads a temperature in degrees Celsius and converts it to degrees Fahrenheit.

# Program introduction
print('Welcome! This program will help you convert temperature from Celsius to Fahrenheit in just a second.')

# The user enters the Temperature in Celsius
temp_Celsius = input('\nEnter the current temperature in Celsius(eg.: 25°C): ')

# Remove "°C" and convert string back to float
temp_Celsius = float(temp_Celsius.replace('°C','').replace('ºC','').strip())

# Convert from Celsius to Fahrenheit
temp_fahrenheit = temp_Celsius * 9/5 + 32

# Return the temperature converted on the terminal
print(f'\nThe temperature {temp_Celsius}°C converted to Fahrenheit is: {temp_fahrenheit:.1f}°F')

# Bonus
temp_kelvin = temp_Celsius + 273.15
print(f'Bonus! The temperature converted to Kelvin is: {temp_kelvin}K')
