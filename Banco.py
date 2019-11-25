#Axel Igor Aviloff
#Algoritmos e programação UFFS 19.1

from ValidaCpf import isCpfValid
from ValidaEmail import isValidEmail
from Cliente import Cliente
from random import randint
from time import sleep
import os #Módulo importado para conseguir usar comandos do próprio terminal

#Dicionário de cores que serão utilizadas para estilizar o terminal.
cores = {"limpa":"\033[m",
         "vermelho":"\033[31m",
         "branco":"\033[30m",
         "piscar":"\033[5m",
         "fundobranco":"\033[7m",
         "cinza":"\033[100m",
         "verde":"\033[32m"
}

#Limpa tela do terminal
def limpaTela():
    os.system('cls' if os.name == 'nt' else 'clear')

#Exibe o menu de opções do sistema.
def mostraMenu():
    print("""       ___              _   
 __ __| _ ) __ _  _ _  | |__
 \ V /| _ \/ _` || ' \ | / /
  \_/ |___/\__,_||_||_||_\_\ 
""")
    print("-------------------------------")
    print("""[1] Inserir cliente
[2] Alterar dados de um cliente
[3] Excluir cliente
[4] Listar clientes
[5] Movimento da conta
[6] Sair""")

#se opcao_menu == 1 realiza o cadastro de clientes, onde cada instância de Cliente é armazenada em um list.
def cadastraCliente():
    limpaTela()
    print("{}=========== CADASTRO DE CLIENTES ==========={}".format(cores["cinza"], cores["limpa"]))
    print("Preencha os campos ou digite 1 para voltar ao menu principal.\n")
    
    cpf = str(input("CPF: "))
    if cpf == "1":
        return
    while (isCpfValid(cpf) == False) or (cpfExiste(cpf)):
        cpf = str(input("{}CPF inválido ou já cadastrado. Digite novamente (ou digite 1 para voltar):\n{}".format(cores["vermelho"], cores["limpa"])))
        if cpf == "1":
            return
    
    nome = str(input("Primeiro nome: "))
    if nome == "1":
        return

    sobrenome = str(input("Sobrenome: "))
    if sobrenome == "1":
        return
    
    email = str(input("Email: "))
    if email == "1":
        return
    while (not(isValidEmail(email))):
        email = str(input("{}Email inválido. Digite novamente (ou digite 1 para voltar):\n{}".format(cores["vermelho"], cores["limpa"])))
        if email == "1":
            return
    
    endereco = str(input("Endereço: "))
    if endereco == "1":
        return
    
    telefone = str(input("Telefone: "))
    if telefone == "1":
        return
    
    numeroconta = randint(10000, 99999)
    while contaExiste(numeroconta):
        numeroconta = randint(10000, 99999)
    
    c = Cliente(nome, sobrenome, cpf, email, endereco, telefone, numeroconta, 1000.0, 0.0)
    
    print("\nCadastrando cliente...\n")
    sleep(1)
    print("Cliente cadastrado com sucesso!\nNúmero da conta: {}{}{}\n".format(cores["fundobranco"],numeroconta, cores["limpa"]))
    sleep(2)
    
    clientes.append(c)


#se opcao_menu == 2 percorre a list de clientes e muda o atributo desejado.
def alteraCliente():
    limpaTela()
    print("{}=========== ALTERAÇÃO DE CLIENTES ==========={}\n".format(cores["cinza"], cores["limpa"]))
    
    cpf_consulta = str(input("Digite CPF do cliente (ou digite 1 para voltar): "))
    while not(cpfExiste(cpf_consulta)) and cpf_consulta != "1":
        cpf_consulta = str(input("{}Esse CPF não está cadastrado no sistema ou é inválido. Digite novamente (ou digite 1 para voltar):\n{} ".format(cores["vermelho"], cores["limpa"])))
    if cpf_consulta == "1":
        return
    
    for cliente in clientes:
        if cliente.cpf == cpf_consulta:
            dado = input("\nQue informação da conta você deseja alterar?\n[1] Endereço\n[2] Email\n[3] Telefone\n[4] Voltar\n => ")
            while dado not in ["1","2","3","4"]:
                dado = input(" => ")
            if dado == "1":
                cliente.endereco = str(input("Digite o novo endereço: "))
            elif dado == "2":
                cliente.email = str(input("Digite o novo email: "))
            elif dado == "3":
                cliente.telefone = str(input("Digite o novo telefone: "))
            elif dado == "4":
                return
            print("Alterando informações...")
            sleep(1)
            print("Alterações realizadas com sucesso!\n")
            sleep(1)
            break

#se opcao_menu == 3 deleta um cliente através da função deletarCliente() que usa como parâmetro o cpf do cliente a ser deletado.       
def deletaCliente():
    limpaTela()
    print("{}=========== REMOÇÃO DE CLIENTES ==========={}\n".format(cores["cinza"], cores["limpa"]))
    
    cpf = str(input("Digite o CPF do cliente a ser deletado (ou digite 1 para voltar): "))
    while (not(cpfExiste(cpf)) and cpf != "1"):
        cpf = str(input("{}Esse CPF não está cadastrado no sistema ou é inválido. Digite novamente (ou digite 1 para voltar):\n{} ".format(cores["vermelho"], cores["limpa"])))
    if cpf == "1":
        return
    
    nome, sobrenome = obterNome(cpf)    
    confirmacao = input("Você confirma a remoção do cliente {} {} ?\n[1] Sim\n[2] Não\n => ".format(nome, sobrenome))
    while confirmacao not in ["1","2"]:
        confirmacao = input(" => ".format(obterNome(cpf)))
    
    if confirmacao == "1":
        deletarCliente(cpf)
        print("Deletando cliente do sistema...") 
        sleep(1)
        print("Cliente deletado com sucesso!")
        sleep(1)
    elif confirmacao == "2":
        print("Cliente não deletado.")

#se opcao_menu == 4 lista as informações dos clientes percorrendo a lista de clientes e mostrando seus atributos.
def mostraClientes():
    limpaTela()
    print("Carregando lista de clientes...")
    sleep(1)
    limpaTela()
    
    if clientes == []:
        print("\n{}O Sistema não possuí nenhum cliente cadastrado!{}\n".format(cores["vermelho"], cores["limpa"]))
    else:
        print("{}=========== LISTA DE CLIENTES ==========={}".format(cores["cinza"], cores["limpa"]))
        
        for cliente in clientes:
            print()
            print("{}NOME:{} {}".format(cores["verde"], cores["limpa"], cliente.nome))
            print("{}SOBRENOME:{} {}".format(cores["verde"], cores["limpa"], cliente.sobrenome))
            print("{}CPF:{} {}".format(cores["verde"], cores["limpa"], cliente.cpf))
            print("{}EMAIL:{} {}".format(cores["verde"], cores["limpa"], cliente.email))
            print("{}ENDEREÇO:{} {}".format(cores["verde"], cores["limpa"], cliente.endereco))
            print("{}TELEFONE:{} {}".format(cores["verde"], cores["limpa"], cliente.telefone))
            print("{}NÚMERO CONTA CORRENTE:{} {}".format(cores["verde"], cores["limpa"], cliente.conta.numero_conta))
            print("{}LIMITE DE CRÉDITO:{} {}".format(cores["verde"], cores["limpa"], cliente.conta.limite_credito))
            print("{}SALDO:{} {}".format(cores["verde"], cores["limpa"], cliente.conta.saldo))
            print("------------------------------")
    
    x = input("[1] Voltar\n=> ")
    while x != "1":
        x = input("=> ")

#se opcao_menu == 5 o programa realiza operações de crédito e débito na conta.
def movimentoConta():
    limpaTela()
    print("{}=========== MOVIMENTO DA CONTA ==========={}\n".format(cores["cinza"], cores["limpa"]))
    
    operacao = str(input("[1] Crédito\n[2] Débito\n[3] Voltar\n => "))
    while operacao not in ["1","2","3"]:
        operacao = str(input(" => "))
    
    if operacao == "3":
        return   
    
    numero_conta = input("Digite o número da conta (ou digite 1 para voltar): ")
    while (not contaExiste(numero_conta)) and numero_conta != "1":
        numero_conta = input("{}Número de conta não existe ou é inválido. Digite novamente (ou digite 1 para voltar):{}\n".format(cores["vermelho"], cores["limpa"]))
    
    if numero_conta == "1":
        return
    
    numero_conta = int(numero_conta)
    
    if operacao == "1":
        valor = input("Digite o valor a ser creditado na conta {}, R$:".format(numero_conta))
        while creditarConta(numero_conta, valor) == False:
            valor = input("R$")
    
    if operacao == "2":
        valor = input("Digite o valor a ser debitado da conta {}, R$".format(numero_conta))
        while debitarCliente(numero_conta, valor) == False:
            valor = input("R$")

#se opcao_menu == 6 o programa finaliza.
def sair():
    limpaTela()
    print("Encerrando sistema...")
    sleep(1)

#Deleta um cliente através do seu CPF.
def deletarCliente(cpf):
    for cliente in clientes:
        if cliente.cpf == cpf:
            clientes.remove(cliente)

#Verifica se o número da conta já existe no sistema.
def contaExiste(numeroconta):
    try:
        numeroconta = int(numeroconta)
    except:
        return False

    for cliente in clientes:
        if cliente.conta.numero_conta == numeroconta:
            return True
    return False

#Verifica se o CPF já existe no sistema.
def cpfExiste(cpf):
    for cliente in clientes:
        if cliente.cpf == cpf:
            return True
    return False

#Obtem nome do proprietário da conta através do seu CPF.
def obterNome(cpf):
    for cliente in clientes:
        if cliente.cpf == cpf:
            return cliente.nome, cliente.sobrenome

#Deposita um valor no saldo de uma conta.
def creditarConta(numero_conta, valor):
    try:
        valor = float(valor)
    except:
        print("Valor inválido. Digite novamente")
        return False 

    for cliente in clientes:
        if cliente.conta.numero_conta == numero_conta:
            x = cliente.conta.creditar(valor)
            return x

#Debita um valor na conta de um cliente.
def debitarCliente(numero_conta, valor):
    try:
        valor = float(valor)
    except:
        print("Valor inválido. Digite novamente")
        return False 
    
    for cliente in clientes:
        if cliente.conta.numero_conta == numero_conta:
            x = cliente.conta.debitar(valor)
            return x
            
    

#Inicio do programa
limpaTela()
clientes = []
print("Iniciando sistema...")
sleep(1)
limpaTela()

while True:
    limpaTela()
    mostraMenu()
    opcao_menu = input(" => ")
    if opcao_menu == "1":
        cadastraCliente()

    if opcao_menu == "2":
        alteraCliente()
                        
    if opcao_menu == "3":
        deletaCliente()
    
    if opcao_menu == "4":
        mostraClientes()
    
    if opcao_menu == "5":
        movimentoConta()
    
    if opcao_menu == "6":
        sair()
        break