#!/usr/bin/env python3

# Created By: Nathan Araujo
# Date: Nov. 22, 2022
# This program converts the temperature in celsius to fahrenheit


def Temperature():

    # Asks the user for the temperature in Celsius
    temp_C_str = input("Enter the temperature in celsius: ")

    # Try catch to catch if the user entered a string
    try:
        temp_C = float(temp_C_str)
    except:
        print("You must enter the temperature in celsius.")
    else:

        # Converts the temperature to fahrenheit
        tempF = temp_C * 9 / 5 + 32

        # Displays the converted fahrenheit temperature
        print(f"{temp_C} degrees celsius is {tempF} degrees fahrenheit")


def main():

    # Calls the fahrenheit function
    Temperature()


if __name__ == "__main__":
    main()
