class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance!")
acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(300)
acc.withdraw(2000)
print("Current Balance =", acc.balance)