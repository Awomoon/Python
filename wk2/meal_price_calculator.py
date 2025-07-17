# 🍽️ Meal Price Calculator - Milestone
# This program asks for meal prices and number of people, then calculates the subtotal.

# Get meal prices
child_price = float(input("What is the price of a child's meal? "))
adult_price = float(input("What is the price of an adult's meal? "))

# Get number of people
num_children = int(input("How many children are there? "))
num_adults = int(input("How many adults are there? "))

# Calculate subtotal
subtotal = (child_price * num_children) + (adult_price * num_adults)

# Display subtotal
print(f"Subtotal: ${subtotal:.2f}")
