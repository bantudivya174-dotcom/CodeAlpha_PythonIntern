# task2_stock.py

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 130
}

total_investment = 0

print("Available stocks:", list(stock_prices.keys()))

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()
    
    if stock == "DONE":
        break
    
    if stock not in stock_prices:
        print("Stock not available!")
        continue
    
    quantity = int(input("Enter quantity: "))
    
    investment = stock_prices[stock] * quantity
    total_investment += investment

print("Total Investment Value:", total_investment)

# Save result to file
with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment: {total_investment}")
