#!/usr/bin/python3
# This program converts Celcius to Fahrenheit depending on whether
# the user inputs a Celcius or Fahrenheit value

degree = ""
scale = ""
degree_converted = ""

def c_to_f(centigrade):
    fahrenheit = (1.8 * centigrade) + 32.0
    return fahrenheit

def f_to_c(fahrenheit):
    centigrade = (fahrenheit - 32) / 1.8
    return centigrade

def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

while degree != "exit":
    print("This is a temperature converter from Celcius to Fahrenheit and vice versa.")
    degree = input("Enter a numerical degree to convert or type Exit: ")
    if is_number(degree) is True:
        degree = float(degree)
        scale = input("Which scale are you converting from? Enter C for Celcius or F for Fahreinheit: ")
        if scale.lower() == "f":
            degree_converted = f_to_c(degree)
            print(degree, "Fahrenheit equals", degree_converted, "Celcius.\n")
        elif scale.lower() == "c":
            degree_converted = c_to_f(degree)
            print(degree, "Celcius equals", degree_converted, "Fahrenheit.\n")
        else:
            print("I don't understand. Please try again.\n")
    else:
        if degree.lower() == "exit":
            degree = degree.lower()
            print("Goodbye.\n")
        else:
            print("I don't understand. Please try again.\n")