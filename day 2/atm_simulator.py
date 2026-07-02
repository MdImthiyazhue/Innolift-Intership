# PyBank ATM Simulator

# Initial account details
balance = 5000
transaction_count = 0
correct_pin = "4416"

# PIN Verification (3 attempts)
for attempt in range(3):
    pin = input("Enter your 4-digit PIN: ")

    if pin == correct_pin:
        print("\nLogin Successful!\n")
        break
    else:
        print("Incorrect PIN.")

# Lock the user after 3 failed attempts
else:
    print("\nToo many incorrect attempts. Your account has been locked.")
    exit()

# Main ATM menu
while True:
    print("\n====== PYBANK ATM ======")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Choose an option: ")

    # Option 1 - Check Balance
    if choice == "1":
        print(f"Current Balance: ₹{balance}")

    # Option 2 - Deposit
    elif choice == "2":
        amount = float(input("Enter deposit amount: ₹"))

        if amount > 0:
            balance += amount
            transaction_count += 1
            print(f"Deposit Successful! New Balance: ₹{balance}")
        else:
            print("Invalid amount. Deposit must be greater than zero.")

    # Option 3 - Withdraw
    elif choice == "3":
        amount = float(input("Enter withdrawal amount: ₹"))

        if amount > 0:
            if amount <= balance:          # Nested if
                balance -= amount
                transaction_count += 1
                print(f"Withdrawal Successful! New Balance: ₹{balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid amount. Withdrawal must be greater than zero.")

    # Option 4 - Exit
    elif choice == "4":
        print("\n===== SESSION SUMMARY =====")
        print(f"Final Balance: ₹{balance}")
        print(f"Successful Transactions: {transaction_count}")
        print("Thank you for using PyBank ATM!")
        break

    # Invalid menu choice
    else:
        print("Invalid option. Please choose between 1 and 4.")