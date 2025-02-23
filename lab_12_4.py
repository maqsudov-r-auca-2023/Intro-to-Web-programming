class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited {amount}. New balance: {self.__balance}"
        return "Invalid deposit amount"

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew {amount}. Remaining balance: {self.__balance}"
        return "Insufficient funds"

    def get_balance(self):
        return self.__balance

account = BankAccount("12345678", 1000)

print(account.deposit(500))
print(account.withdraw(200))
print(account.get_balance())
