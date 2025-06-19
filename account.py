# account.py

class Account:
    def __init__(self, number, owner, balance=0.0):
        self.number = number
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited R${amount:.2f}")
        else:
            print("Invalid amount to deposited.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew R${amount:.2f}")
        else:
            print("Insufficient funds or invalid amount.")
    
    def get_balance(self):
        return self.balance
    
    def __str__(self):
        return f"Account {self.number} - Owner: {self.owner}, Balance: R${self.balance:.2f}"