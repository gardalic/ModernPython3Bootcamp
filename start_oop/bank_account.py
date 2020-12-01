"""
    Define class BankAccount. Each BankAccount has an owner, and a balance_attribute that starts at 0.0. The class should have methods to withdraw money, and deposit. 
"""


class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount
        print(f"Withdrew {amount}, new balance {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}, new balance: {self.balance}")


acct = BankAccount("Darcy")

acct.deposit(10)
acct.withdraw(3)
