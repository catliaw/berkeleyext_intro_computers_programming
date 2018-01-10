#!/usr/bin/python3
# This script converts degrees Celcius into degrees Fahrenheit.

# Input from user for degrees Celcius to convert into degrees Fahrenheit
centigrade = float(input("Please input temperature in Celcius: "))

# F = (1.8*C) + 32
fahrenheit = (1.8 * centigrade) + 32.0

# Print out conversion into standard output.
print(centigrade, "Celcius equals", fahrenheit, "Fahrenheit.")
