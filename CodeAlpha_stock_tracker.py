stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320
}

total_value = 0

while True:

    stock = input("Enter stock name (or 'done' to finish): ")

    if stock == "done":
        break

    if stock not in stocks:
        print("Stock not found.")
        continue

    quantity = int(input("Enter quantity: "))

    price = stocks[stock]
    value = price * quantity

    total_value += value

    print("Value:", value)

print("Total Investment Value:", total_value)

file = open("portfolio.txt", "w")
file.write("Total Investment: " + str(total_value))
file.close()