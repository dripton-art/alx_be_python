num1 = input("Enter first number: ")
operation = input("Choose the operation (+, -, /, *): ")
num2 = input("Enter second number: ")



match operation:
    case "+":
        result = num1 + num2
        print(f"The result is [result]")
    case "-":
        result = num1 - num2
        print(f"The result is [result]")
    case "*":
        result = num1 * num2
        print(f"The result is [result]")
    case "/":
        if num2 == 0:
            print("cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is [result]")
    case _:
        print("invalid operation!")