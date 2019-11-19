class Conta:

    def __init__(self, numero_conta, limite_credito, saldo):
        self.numero_conta = numero_conta
        self.limite_credito = limite_credito
        self.saldo = saldo
    
    def debitar(self, valor):
        self.saldo -= valor
    
    def creditar(self, valor):
        self.saldo += valor