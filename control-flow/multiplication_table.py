number = int(input("Enter a number to see its multiplication table: "))
X = number
for Y in range(1, 11):
    Z = X * Y
    print("{X} * {Y} = {Z}")