from Conta import Conta

class Cliente:
    
    def __init__(self, nome, sobrenome, cpf, email, endereco, telefone, numero_conta, limite_credito, saldo):
        self.conta = Conta(numero_conta, limite_credito, saldo)
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.email = email
        self.endereco = endereco
        self.telefone = telefone
    



