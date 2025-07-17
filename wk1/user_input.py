"""
Programme: Moon-Tour.
Authour: Moontech.

Description: Helps users book a Tour and also Register.
"""

# Welcome message
print("Welcome to Moon-Tour")
print()

# Registeration
name = input("Please input your name for registration: ")
age = input("Please input your age: ")
current_location = input("Please input your current location: ")
vacation_location = input("Where would you like to visit for your vacation? ")
days = input("How many days would you like to spend on your vacation? ")
print()

# Output
print(f"{name} of age {age} currently living at {current_location} is spending {days} days in {vacation_location}.")
