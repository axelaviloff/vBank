from ValidaCpf import isCpfValid
from Cliente import Cliente
from random import randint
clientes = []
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("Sistema vBank Iniciado")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-")

def mostraMenu():
    print("""1. Insere Cliente
2. Altera dados de um cliente
3. Exclui cliente
4. Lista Clientes
5. Movimento da conta
6. Sair""")

def mostraClientes():
    if clientes == []:
        print("\nO Sistema não possuí nenhum cliente cadastrado!\n")
    else:
        for cliente in clientes:
            print()
            print("Nome:", cliente.nome)
            print("Sobrenome:", cliente.sobrenome)
            print("CPF:", cliente.cpf)
            print("Email:", cliente.email)
            print("Endereço:", cliente.endereco)
            print("Telefone", cliente.telefone)
            print("Número da Conta Corrente:", cliente.conta.numero_conta)
            print("Limite de crédito:", cliente.conta.limite_credito)

def deletarCliente(cpf):
    for cliente in clientes:
        if cliente.cpf == cpf:
            clientes.remove(cliente)

def verificaNumeroConta(numeroconta):
    for cliente in clientes:
        if cliente.conta.numero_conta == numeroconta:
            return False
    return True

def cpfExists(cpf):
    for cliente in clientes:
        if cliente.cpf == cpf:
            return True
    return False


while True:
    print()
    mostraMenu()
    opcao_menu = int(input("\nDigite uma opção => "))
    if opcao_menu == 1:
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
        print("\nConta criada com sucesso!\nNúmero da conta: {}".format(numeroconta))
        numeroconta += 1
        clientes.append(c)

    if opcao_menu == 2:
        cpf_consulta = str(input("Digite seu CPF: "))
        while not(cpfExists(cpf_consulta)):
            cpf_consulta = str(input("Esse CPF não está cadastrado no sistema ou é inválido. Digite novamente: "))
        for cliente in clientes:
                if cliente.cpf == cpf_consulta:
                    dado = int(input("O que você deseja mudar na conta?\n1. Endereço\n2. Email\n3. Telefone:\n4. Voltar"))
                    while dado not in [1,2,3,4]:
                        dado = int(input("Opção inválida. Digite novamente:"))
                        if dado == 1:
                            cliente.endereco = str(input("Digite o novo endereço: "))
                        elif dado == 2:
                            cliente.email = str(input("Digite o novo email: "))
                        elif dado == 3:
                            cliente.telefone = str(input("Digite o novo telefone: "))
                        elif dado == 4:
                            break
    if opcao_menu == 3:
        cpf = str(input("Digite o CPF do cliente a ser deletado:\n"))
        deletarCliente(cpf)
    
    if opcao_menu == 4:
        mostraClientes()
    
    if opcao_menu == 6:
        break
        
        
