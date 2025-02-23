def withdraw(amount, balance):
    if amount > balance:
        raise ValueError("Insufficient balance.")
    return balance - amount

try:
    print("New balance:", withdraw(100, 50))
except ValueError as e:
    print("Error:", e)