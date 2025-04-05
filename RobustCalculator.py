def calculator(a, b, operator):
    try:
        a = int(a)
        b = int(b)
        
        if operator == "+":
            return a + b
        elif operator == "-":
            return a - b
        elif operator == "*":
            return a * b
        elif operator == "/":
            if b == 0:
                return "Error: Division by zero"
            else:
                return a / b
        elif operator == "%":
            if b == 0:
                return "Error: Modulo by zero"
            else:
                return a % b
        elif operator == "**":
            return a ** b
        else:
            return "Error: Unsupported operator"
    except:
        return "Error: Invalid input"

print(calculator(10, 0, "/"))
print(calculator(10, "five", "+"))
print(calculator(10, 5, "$"))
print(calculator(2, 3, "**"))

