class Conta:

    def __init__(self, numero_conta, limite_credito, saldo):
        self.numero_conta = numero_conta
        self.limite_credito = limite_credito
        self.saldo = saldo
    
    def debitar(self, valor):
        if self.saldo + valor > 0:
            self.saldo += valor
        else:
            print("Impossível debitar esse valor")
    
    def creditar(self, valor):
        if self.limite_credito + valor > 0:
            self.limite_credito += valor