class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


account = BankAccount("Aryan", 5000)

account.deposit(2000)

print("Account Holder:", account.owner)
print("Balance:", account.get_balance())
