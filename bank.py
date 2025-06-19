# bank.py

from client import Client
from account import Account

class Bank:
    def __init__(self):
        self.clients = []
        self.accounts = []

    def register_client(self, name, cpf):
        if self.find_client_by_cpf(cpf):
            print("Já existente um cliente com esse CPF.")
            return None
        client = Client(name, cpf)
        self.clients.append(client)
        print(f"Client {name}, registered successfully.")
        return client
    
    def create_account(self, client, account_number):
        account = Account(account_number, owner=client.name)
        client.add_account(account)
        self.accounts.append(account)
        print(f"Account {account_number} created for {client.name}")
        return account

    def find_client_by_cpf(self, cpf):
        for client in self.clients:
            if client.cpf == cpf:
                return client
        print("Client not found.")
        return None
    
    def list_accounts(self):
        for acc in self.accounts:
            print(acc)
