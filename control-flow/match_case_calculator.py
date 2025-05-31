num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Choose the operation (+, -, /, *): ")

result1 = num1 + num2
result2 = num1 - num2
result3 = num1 * num2
result4 = num1 / num2

match operation:
    case "+":
        print(f"The result is {result1}")
    case "-":
        print(f"The result is {result2}")
    case "*":
        print(f"The result is {result3}")
    case "/":
        if num2 == 0:
            print("cannot divide by zero.")
        else:
            print(f"The result is {result4}")
    case _:
        print("invalid operation!")