# ==========================================
# SIMPLE CALCULATOR PROGRAM IN PYTHON
# ==========================================

# ----------- Function Definitions ----------

def add(a, b):
    """Function to add two numbers"""
    return a + b


def subtract(a, b):
    """Function to subtract two numbers"""
    return a - b


def multiply(a, b):
    """Function to multiply two numbers"""
    return a * b


def divide(a, b):
    """Function to divide two numbers"""
    if b == 0:
        return "Error! Division by zero is not allowed."
    else:
        return a / b


def show_menu():
    """Function to display calculator menu"""
    print("\n========= CALCULATOR MENU =========")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("==================================")


# -------------- Main Program ---------------

print("WELCOME TO PYTHON CALCULATOR")

while True:
    # Display menu
    show_menu()

    # Take user choice
    choice = input("Enter your choice (1-5): ")

    # Exit condition
    if choice == '5':
        print("Thank you for using the calculator!")
        break

    # Input numbers
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values only.")
        continue

    # Perform selected operation
    if choice == '1':
        result = add(num1, num2)
        print("Result:", result)

    elif choice == '2':
        result = subtract(num1, num2)
        print("Result:", result)

    elif choice == '3':
        result = multiply(num1, num2)
        print("Result:", result)

    elif choice == '4':
        result = divide(num1, num2)
        print("Result:", result)

    else:
        print("Invalid choice! Please select between 1 and 5.")

    print("----------------------------------")
