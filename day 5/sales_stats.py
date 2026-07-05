import numpy as np

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

sales = np.array([5200, 6100, 4700, 8000, 7200, 6900, 5400])

average = sales.mean()

print("===== Weekly Sales =====")

for d, s in zip(days, sales):
    print(f"{d}: ₹{s}")

print()

print("Average :", average)
print("Maximum :", sales.max())
print("Minimum :", sales.min())
print("Total   :", sales.sum())

above_average = sales > average

print()
print("Days Above Average:", np.sum(above_average))