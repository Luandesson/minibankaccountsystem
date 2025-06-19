# main.py

from bank import Bank
def is_valid_cpf(cpf):
    cpf = cpf.replace(".","").replace("-","")
    return cpf.isdigit() and len(cpf) == 11

def select_account(client):
    if len(client.accounts) > 1:
        print("Contas disponíveis:")
        for i, acc in enumerate(client.accounts):
            print (f"{i+1}. {acc}")
        while True:
            try:
                index = int(input("Escolha o número da conta: ")) -1
                if 0 <= index < len(client.accounts):
                    return index
                else:
                    print("Número inválido.")
            except ValueError:
                print("Por favor, digite um número válido.")
    return 0
    
def main():
    bank = Bank()

    while True:
        print("\n====== MINI BANK SYSTEM ======")
        print("1. Cadastrar cliente")
        print("2. Criar conta")
        print("3. Depositar")
        print("4. Sacar")
        print("5. Ver saldo")
        print("6. Listar contas")
        print("0. Sair")

        option = input("Escolha uma opção: ")

        if option == "1":
            name = input("Nome do cliente: ")
            cpf = input("CPF do cliente: ")
            if not is_valid_cpf(cpf):
                print("CPF inválido. Deve conter 11 números.")
                continue

            bank.register_client(name, cpf)

        elif option == "2":
            cpf = input("CPF do cliente para vincular a conta: ")
            client = bank.find_client_by_cpf(cpf)
            if client:
                acc_number = input("Número da nova conta: ")
                bank.create_account(client, acc_number)

        elif option == "3":
            cpf = input("CPF do cliente: ")
            client = bank.find_client_by_cpf(cpf)
            if client and client.accounts:
                acc_index = select_account(client)
                while True:
                    try:
                        amount_str = input("Valor do depósito: ")
                        amount = float(amount_str.replace(".","").replace(".","."))
                        if amount <= 0:
                            print("O valor deve ser positivo.")
                        else:
                            break
                    except ValueError:
                        print("Por favor, digite um número válido.")
                client.accounts[acc_index].deposit(amount)
            else:
                print("Cliente não encontrado ou sem conta.")

        elif option == "4":
            cpf = input("CPF do cliente: ")
            client = bank.find_client_by_cpf(cpf)
            if client and client.accounts:
                acc_index = select_account(client)
                while True:
                    try:
                        amount_str = input("Valor do saque: ")
                        amount = float(amount_str.replace(".","").replace(",","."))
                        if amount <= 0:
                            print("O valor deve ser positivo.")
                        elif amount > client.accounts[acc_index].get_balance():
                            print("Saldo insuficiente.")
                        else:
                            client.accounts[acc_index].withdraw(amount)
                            break                         
                    except ValueError:
                        print("Por favor, digite um número válido.")
            else:
                print("Cliente não encontrado ou sem conta.")

        elif option == "5":
            cpf = input("CPF do cliente: ")
            client = bank.find_client_by_cpf(cpf)
            if client and client.accounts:
                print(f"\nContas de {client.name}:")
                for i, acc in enumerate(client.accounts):
                    print(f"{i+1}. {acc}")
            else:
                print("Cliente não encontrado ou sem conta.")
               
        elif option == "6":
            cpf = input("CPF do cliente para visualizar contas: ")
            client = bank.find_client_by_cpf(cpf)
            if client and client.accounts:
                print(f"\nContas vinculadas ao CPF {cpf}:")
                for acc in client.accounts:
                    print(acc)
            else:
                print("Cliente não encontrado ou sem contas.")

        elif option == "0":
            print("Encerrando o sistema. Até mais!!")
            break

if __name__ == "__main__":
    main()               
        