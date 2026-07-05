import numpy as np

items = ["Rice", "Milk", "Bread", "Eggs", "Juice"]

prices = np.array([60, 45, 35, 7, 120])
quantities = np.array([2, 3, 2, 12, 1])

line_totals = prices * quantities

print("===== Grocery Bill =====")

for item, qty, price, total in zip(items, quantities, prices, line_totals):
    print(f"{item:10} Qty:{qty} Price:{price} Total:{total}")

print("---------------------------")
print(f"Grand Total = ₹{line_totals.sum()}")