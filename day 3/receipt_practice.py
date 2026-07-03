# Flexible Receipt Builder

def build_receipt(**details):
    receipt = ""

    for key, value in details.items():
        receipt += f"{key}: {value}\n"

    return receipt


# Receipt 1
print("Receipt 1")
print(build_receipt(
    customer="Afsin",
    amount=500,
    type="Deposit"
))

# Receipt 2
print("Receipt 2")
print(build_receipt(
    customer="Imthiyas",
    amount=1200,
    type="Purchase",
    payment="UPI"
))