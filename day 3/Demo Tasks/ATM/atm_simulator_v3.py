from bank_utils import format_currency, is_valid_amount, build_log_line

balance = 5000
LOG_FILE = "transactions.log"


def save_log(action, amount):
    with open(LOG_FILE, "a") as file:
        file.write(build_log_line(action, amount, balance))


while True:

    print("\n===== PYBANK ATM =====")
    print("1. Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. View History")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        print("Balance:", format_currency(balance))

    elif choice == "2":
        amount = float(input("Deposit Amount: "))

        if is_valid_amount(amount):
            balance += amount
            save_log("Deposit", amount)
            print("Deposit Successful")
        else:
            print("Invalid Amount")

    elif choice == "3":
        amount = float(input("Withdraw Amount: "))

        if is_valid_amount(amount) and amount <= balance:
            balance -= amount
            save_log("Withdraw", amount)
            print("Withdrawal Successful")
        else:
            print("Invalid Transaction")

    elif choice == "4":

        try:
            with open(LOG_FILE, "r") as file:
                print(file.read())
        except FileNotFoundError:
            print("No Transactions Found")

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")