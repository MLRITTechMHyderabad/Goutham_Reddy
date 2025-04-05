import numpy as np

stock_prices = np.array([
    [120, 340, 450, 220, 310],
    [330, 420, 380, 250, 410],
    [150, 280, 290, 230, 200],
])

print("Average stock prices:")
for col in range(5):
    total = 0
    for row in range(3):
        total = total + stock_prices[row][col]
    average = total / 3
    print("Company", col + 1, ":", round(average, 1))

highest = stock_prices[0][0]
day = 0
company = 0
for i in range(3):
    for j in range(5):
        if stock_prices[i][j] > highest:
            highest = stock_prices[i][j]
            day = i
            company = j
print("\nHighest price recorded:", highest)
print("Day:", day + 1)
print("Company:", company + 1)

min_val = stock_prices[0][0]
max_val = stock_prices[0][0]
for i in range(3):
    for j in range(5):
        if stock_prices[i][j] < min_val:
            min_val = stock_prices[i][j]
        if stock_prices[i][j] > max_val:
            max_val = stock_prices[i][j]

print("\nNormalized prices:")
for i in range(3):
    row = []
    for j in range(5):
        norm = (stock_prices[i][j] - min_val) / (max_val - min_val)
        row.append(round(norm, 2))
    print(row)

print("\n⚠️ Risky Investment Days:")
for i in range(3):
    risky = []
    for j in range(5):
        if stock_prices[i][j] < 200:
            risky.append(stock_prices[i][j])
    if len(risky) > 0:
        print("Day", i + 1, ":", risky)
