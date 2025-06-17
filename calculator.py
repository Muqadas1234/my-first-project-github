


def calculator():
    print("📢 Welcome to Muqadas' Calculator!\n")
    print("🔢 Simple Calculator")
    
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                result = "Error: Cannot divide by zero."
            else:
                result = num1 / num2
        else:
            result = "Invalid operator!"

        print("Result:", result)
        
    except ValueError:
        print("Please enter valid numbers.")

# 🔽 THIS LINE IS VERY IMPORTANT!
if __name__ == "__main__":
    calculator()
