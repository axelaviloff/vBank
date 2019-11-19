from ValidaCpf import isCpfValid
from Cliente import Cliente
from random import randint
from time import sleep
import os
os.system('cls' if os.name == 'nt' else 'clear')
clientes = []
print("Iniciando sistema...")
sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
print("""       ___              _   
 __ __| _ ) __ _  _ _  | |__
 \ V /| _ \/ _` || ' \ | / /
  \_/ |___/\__,_||_||_||_\_\ 
""")


#Exibe o menu de opções do sistema
def mostraMenu():
    print("-------------------------------")
    print("""1. Inserir Cliente
2. Alterar dados de um cliente
3. Excluir cliente
4. Listar Clientes
5. Movimento da conta
6. Sair""")

#Mostra todas informações de todos os clientes
def mostraClientes():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Carregando lista de clientes...")
    sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    if clientes == []:
        print("\nO Sistema não possuí nenhum cliente cadastrado!\n")
    else:
        print("== CLIENTES ==")
        for cliente in clientes:
            print()
            print("Nome:", cliente.nome)
            print("Sobrenome:", cliente.sobrenome)
            print("CPF:", cliente.cpf)
            print("Email:", cliente.email)
            print("Endereço:", cliente.endereco)
            print("Telefone:", cliente.telefone)
            print("Número da Conta Corrente:", cliente.conta.numero_conta)
            print("Limite de crédito:", cliente.conta.limite_credito)
            print("Saldo:", cliente.conta.saldo)
            print()

#Deleta um cliente através do seu CPF
def deletarCliente(cpf):
    for cliente in clientes:
        if cliente.cpf == cpf:
            clientes.remove(cliente)

#Verifica se o número da conta já existe no sistema
def verificaNumeroConta(numeroconta):
    for cliente in clientes:
        if cliente.conta.numero_conta == numeroconta:
            return False
    return True

#Verifica se o CPF já existe no sistema
def cpfExists(cpf):
    for cliente in clientes:
        if cliente.cpf == cpf:
            return True
    return False

#Obtem nome do proprietário da conta através do seu CPF
def obterNome(cpf):
    for cliente in clientes:
        if cliente.cpf == cpf:
            return cliente.nome, cliente.sobrenome

#Deposita um valor no saldo de uma conta
def creditarConta(numeroConta, valor):
    for cliente in clientes:
        if cliente.conta.numero_conta == numeroConta:
            cliente.conta.creditar(valor)

def debitarConta(numeroConta, valor):
    for cliente in clientes:
        if cliente.conta.numero_conta == numeroConta:
            cliente.conta.debitar(valor)

#Inicio do programa
while True:
    mostraMenu()
    opcao_menu = input("=> ")
    if opcao_menu == "1":
        cpf = str(input("CPF: "))
        while (isCpfValid(cpf) == False) or (cpfExists(cpf)):
            cpf = str(input("CPF inválido ou já cadastrado. Digite novamente: "))
        nome = str(input("Primeiro nome: "))
        sobrenome = str(input("Sobrenome: "))
        email = str(input("Email: "))
        endereco = str(input("Endereço: "))
        telefone = str(input("Telefone: "))
        numeroconta = randint(10000, 99999)
        while verificaNumeroConta(numeroconta) == False:
            numeroconta = randint(10000, 99999)
        c = Cliente(nome, sobrenome, cpf, email, endereco, telefone, numeroconta, 1000, 0)
        print("\nCadastrando cliente...")
        sleep(2)
        print("Cliente cadastrado com sucesso!\nNúmero da conta: {}\n".format(numeroconta))
        sleep(2)
        clientes.append(c)

    if opcao_menu == "2":
        cpf_consulta = str(input("Digite seu CPF: "))
        while not(cpfExists(cpf_consulta)):
            cpf_consulta = str(input("Esse CPF não está cadastrado no sistema ou é inválido. Digite novamente: "))
        for cliente in clientes:
                if cliente.cpf == cpf_consulta:
                    dado = int(input("Que informação da conta você deseja alterar?\n1. Endereço\n2. Email\n3. Telefone\n4. Voltar\n"))
                    while dado not in [1,2,3,4]:
                        dado = int(input("Opção inválida. Digite novamente:\n"))
                    if dado == 1:
                        cliente.endereco = str(input("Digite o novo endereço: "))
                    elif dado == 2:
                        cliente.email = str(input("Digite o novo email: "))
                    elif dado == 3:
                        cliente.telefone = str(input("Digite o novo telefone: "))
                    elif dado == 4:
                        break
                    print("Alterando informações...")
                    sleep(2)
                    print("Alterações realizadas com sucesso!\n")
                    sleep(2)
                    break
                        
    if opcao_menu == "3":
        cpf = str(input("Digite o CPF do cliente a ser deletado: "))
        while not(cpfExists(cpf)):
            cpf = str(input("Esse CPF não está cadastrado no sistema ou é inválido. Digite novamente: "))
        nome, sobrenome = obterNome(cpf)
        confirmacao = int(input("Você confirma a remoção da conta de {} {} ?\n1. Sim\n2. Não\n".format(nome, sobrenome)))
        while confirmacao not in [1,2]:
            confirmacao = ("Você confirma a remoção da conta de {} ?\n1. Sim\n2. Não\n".format(obterNome(cpf)))
        if confirmacao == 1:
            deletarCliente(cpf)
            print("Deletando conta...")
            sleep(2)
            print("Conta deletada com sucesso!")
        else:
            print("Conta não deletada.")
    
    if opcao_menu == "4":
        mostraClientes()
    
    if opcao_menu == "5":
        operacao = int(input("1. Crédito\n2. Débito\n3. Sair\n "))
        while operacao not in [1,2,3]:
            operacao = int(input("1. Crédito\n2. Débito\n3. Sair\n "))
        if operacao == 3:
            continue   
        numero_conta = int(input("Digite o número da conta: "))
        while verificaNumeroConta(numero_conta):
            numero_conta = int(input("Número de conta inválido. Digite novamente: "))
        if operacao == 1:
            valor = float(input("Digite o valor a ser creditado da conta {}, R$:".format(numero_conta)))
            creditarConta(numero_conta, valor)
        if operacao == 2:
            valor = float(input("Digite o valor a ser debitado da conta {}, R$".format(numero_conta)))
            debitarConta(numero_conta, valor)
    
    if opcao_menu == "6":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nEncerrando sistema...")
        sleep(2)
        break