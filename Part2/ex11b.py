# TODO:
# Create a function called calculate that takes three arguments:
# - A number
# - An operator ("+", "-", "*", or "/")
# - Another number
# The function should return the result of the calculation

# Insert your function code here
def calculate(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Cannot divide by zero"
    else:
        return "Error: Invalid operator"

# Test the function with different operations
print(calculate(35, "+", 1))  # should return 36
print(calculate(15, "-", 1))  # should return 14
print(calculate(1, "*", 10))  # should return 10
print(calculate(10, "/", 10))  # should return 1.0
