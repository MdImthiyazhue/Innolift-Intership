from datetime import datetime

def format_currency(amount):
    return f"Rs. {amount:.2f}"

def is_valid_amount(amount):
    return amount > 0

def build_log_line(action, amount, balance):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"{time} | {action} | Rs. {amount} | Balance: Rs. {balance}\n"