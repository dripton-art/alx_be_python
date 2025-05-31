num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Choose the operation (+, -, /, *): ")

result = num1 + num2
result = num1 - num2
result = num1 * num2
result = num1 / num2

match operation:
    case "+":
        print("The result is {result}")
    case "-":
        print("The result is {result}")
    case "*":
        print("The result is {result}")
    case "/":
        if num2 == 0:
            print("cannot divide by zero.")
        else:
            print("The result is {result}")
    case _:
        print("invalid operation!")