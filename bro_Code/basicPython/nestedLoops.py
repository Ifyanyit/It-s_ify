rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter any symbol you like: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()