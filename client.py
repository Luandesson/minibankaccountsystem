# client.py

class Client:
    def __init__(self, name, cpf):
        self.name = name
        self.cpf = cpf
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def __str__(self):
        return f"Client: {self.name} - CPF: {self.cpf}"
            