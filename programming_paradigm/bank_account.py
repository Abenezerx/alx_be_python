class BankAccount:
    def __init__(self, initial_balance = 0):
        self.account_balance = initial_balance

    def deposit(self, amout):
        self.account_balance += amout

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            return False
    
    def diplay_balance(self):
        print(f'your account balance is {self.account_balance: .2f}')