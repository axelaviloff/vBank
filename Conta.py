from time import sleep

class Conta:

    def __init__(self, numero_conta, limite_credito, saldo):
        self.numero_conta = numero_conta
        self.limite_credito = limite_credito
        self.saldo = saldo
    
    def debitar(self, valor): 
        saldoAnterior = self.saldo
        limiteAnterior = self.limite_credito
        if valor < 0:
            print("Valor deve ser positivo. Digite o valor novamente")
            sleep(1)
            return False
        if (self.saldo + self.limite_credito) - valor >= 0:
            if valor >= self.saldo:
                valor = valor - self.saldo
                self.saldo -= self.saldo
                self.limite_credito = self.limite_credito - valor
                print("\nDebitando...")
                sleep(1)
                print("-----------------------------------")
                print("Saldo anterior R$", saldoAnterior)
                print("Novo saldo R$", self.saldo)
                print("Limite de crédito anterior R$", limiteAnterior)
                print("Novo limite de cŕedito R$", self.limite_credito)
                print("-----------------------------------")
                x = input("[1] Voltar\n=> ")
                while x != "1":
                    x = input("=> ")
                return True
            else:
                self.saldo = self.saldo - valor
                print("\nDebitando...")
                sleep(1)
                print("-----------------------------------")
                print("Saldo anterior R$", saldoAnterior)
                print("Novo saldo R$", self.saldo)
                print("-----------------------------------")
                x = input("[1] Voltar\n=> ")
                while x != "1":
                    x = input("=> ")
                return True
        else:
            print("Valor negativo da conta não pode ser superior ao limite. Digite o valor novamente")
            sleep(1)
            return False
    
    def creditar(self, valor):
        saldoAnterior = self.saldo
        
        if valor > 0:
            self.saldo += valor
            print("\nCreditando...")
            sleep(1)
            print("-----------------------------------")
            print("Saldo anterior R$", saldoAnterior)
            print("Novo saldo R$", self.saldo)
            print("-----------------------------------")
            x = input("[1] Voltar\n=> ")
            while x != "1":
                x = input("=> ")
            return True
        else:
            print("Não é possíve creditar um valor negativo. Digite o valor novamente")
            return False