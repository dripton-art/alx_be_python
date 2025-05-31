num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Choose the operation (+, -, /, *): ")


match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 == 0:
            print("cannot divide by zero.")
        else:
            result = num1 / num2
    case _:
        print("invalid operation!")
print("The result is [result]")
