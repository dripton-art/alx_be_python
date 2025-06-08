# Global variables

CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

def convert_to_celsius(fahrenheit):
    # Subtract 32 to remove Fahrenheit's offset from the Celsius scale
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR 

def convert_to_fahrenheit(celsius):
    # Add 32 to shift from Celsius zero point to Fahrenheit scale
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32 

temp = float(input("Enter the temperature to convert: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

if unit == "C":
    print(f"{temp} is {convert_to_fahrenheit(temp):.1F}°F")
elif unit == "F":
    print(f"{temp} is {convert_to_celsius(temp):.1F}°C")
else:
    print["Invalid temperature. Please enter a numeric value"]