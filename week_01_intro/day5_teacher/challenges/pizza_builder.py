# Challenge: Build your pizza order using functions! 🍕

# Step 1: Ask for size (small/medium/large)
# Step 2: Ask for 2 toppings
# Step 3: Print a fun order summary

def get_size():
    size = input("Choose a pizza size (small, medium, large): ")
    return size

def get_toppings():
    topping1 = input("Enter first topping: ")
    topping2 = input("Enter second topping: ")
    return topping1, topping2

def make_order(size, topping1, topping2):
    print(f"\nGreat choice! Here's your {size} pizza with {topping1} and {topping2}. 🍕 Enjoy!")

# Your code here!
