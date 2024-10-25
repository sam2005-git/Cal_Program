# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error! Division by zero is not allowed."

# Main program
def calculator():
    print("Select operation:")
    print("1. Multiply")
    print("2. Divide")
    
    # Take input from user
    choice = input("Enter choice (1/2): ")

    if choice in ['1', '2']:
        # Taking inputs for the numbers
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            return "Error! Please enter valid numbers."

        # Perform the chosen operation
        if choice == '1':
            print(f"The result of multiplication: {multiply(num1, num2)}")
        elif choice == '2':
            print(f"The result of division: {divide(num1, num2)}")
    else:
        print("Invalid input. Please select 1 or 2.")

# Run the calculator
calculator()
