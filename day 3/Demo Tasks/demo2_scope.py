# Demo 2 - Scope

balance = 5000

def deposit(current_balance, amount):
    return current_balance + amount

print("Before Deposit:", balance)

balance = deposit(balance, 1000)

print("After Deposit:", balance)