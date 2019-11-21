from time import sleep
class Conta:

    def __init__(self, numero_conta, limite_credito, saldo):
        self.numero_conta = numero_conta
        self.limite_credito = limite_credito
        self.saldo = saldo
    
    def debitar(self, valor): 
        if (self.saldo + self.limite_credito) - valor >= 0:
            self.saldo -= valor
            print("Debitando...")
            sleep(1)
            print("Novo saldo R$", self.saldo)
            sleep(2)
            return True
        else:
            print("Valor negativo da conta não pode ser superior ao limite. Digite o valor novamente")
            sleep(1)
            return False
    
    def creditar(self, valor):
        if self.limite_credito + valor > 0:
            self.limite_credito += valor