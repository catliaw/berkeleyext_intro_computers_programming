#!/usr/bin/python3
# This program identifies leap years on Mars
# In each decade there are 6 leap years that last 669 days
# and 4 normal years that last 668 days.
# Odd years, and years that are divisible by 10 are leap years.
# In a decade, 2000s for example:
# Leap Years (6): 2001, 2003, 2005, 2007, 2009, 2010
# Non-Leap Years (4): 2002, 2004, 2006, 2008
# Odd years = year % 2 == 1
# Years divisible by 10 = year % 10 == 0

year = ""

while year != "exit":
    year = input("Enter a Year or type Exit: ")
    if year.isnumeric():
        year = int(year)
        if year % 2 != 1 and year % 10 != 0:
            print(year, "is not a leap year.")
            print(year, "is not odd or divisible by 10.\n")
        else:
            if year % 2 == 1:
                print(year, "is a leap year.")
                print(year, "is an odd numbered year.\n")
            else:
                print(year, "is a leap year.")
                print(year, "is divisible by 10.\n")
    else:
        if year.lower() == "exit":
            year = year.lower()
            print("Goodbye.")
        else:
            print("I don't understand. Try again.\n")

