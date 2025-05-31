# Prompt the user for a positive integer
length = int(input("Enter the size of the pattern: "))

row = 0

# while loop for rows
while row < size:
    # for loop for printing asterisks in one row
    for col in range(size):
        print("*", end="") # print asterisks
        # Move to the next line after one row is printed
    print() 
    row += 1  # Go to the next row
