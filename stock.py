# Simple Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "INFY": 1550,
    "TCS": 3550
}

portfolio = {}
total_investment = 0

print("=== Stock Portfolio Tracker ===")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Invalid stock symbol.")
        continue

    try:
        qty = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = qty
    except ValueError:
        print("Please enter a valid number.")

print("\n--- Portfolio Summary ---")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = qty * price
    total_investment += value
    print(f"{stock} -> {qty} shares × ₹{price} = ₹{value}")

print(f"\nTotal Investment Value: ₹{total_investment}")