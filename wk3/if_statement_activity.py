first = int(input("What is the first number? "))
second = int(input("What is the second number? "))

if first > second:
    print("The first number is greater")
else:
    print("The first number is not greater")

if first == second:
    print("The numbers are equal")
else:
    print("The numbers are not equal")

if second > first:
    print("The second number is greater")
else:
    print("The second number is not greater")

print() # Blank line

user_animal = input("What is your favorite animal? ")

if user_animal.lower() == "Dragon":
    print("That's my favorite animal too!")
else:
    print("That one is not my favorite.")
