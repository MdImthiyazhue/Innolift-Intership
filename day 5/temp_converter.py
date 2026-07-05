import numpy as np

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

celsius = np.array([31, 33, 30, 29, 34, 35, 32])

fahrenheit = celsius * 9/5 + 32

print("===== Temperature Converter =====")

for d, c, f in zip(days, celsius, fahrenheit):
    print(f"{d:4} {c}°C = {f:.1f}°F")