# Multiplication Table Printer

print("=== Multiplication Table Printer ===")
print("Type 'stop' to exit.\n")

# Keep asking until the user types "stop"
while True:
    number = input("Enter a number: ")

    # Exit condition
    if number.lower() == "stop":
        print("Closing Table Printer.")
        break

    # Convert input to integer
    number = int(number)

    print(f"\nMultiplication Table of {number}")
    print("-" * 25)

    # Print the table from 1 to 10
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

    print()