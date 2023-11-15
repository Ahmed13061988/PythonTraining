# one loop inside another loop


rows = int(input("How many rows: "))
columns = int(input("How many columns: "))
symbols = input("Chose the symbol: ")

for i in range(rows):
    print(symbols, end=" ")
    for x in range(columns):
        print(symbols, end=" ")
    print()
