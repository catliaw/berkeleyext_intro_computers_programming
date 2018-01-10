#!/usr/bin/python3
# This script converts length in centimeter to inches.
# 1 inch = 2.54 cm
# x cm * (1 inch / 2.54 cm) = x in / 2.54

cm = float(input("Please input length in centimeters: "))

inches = cm / 2.54

print(cm, "centimeters equals", inches, "inches.")
