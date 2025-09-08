class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0.0  # saldo inicia em zero

    def exibir_saldo(self):
        print(f"Titular: {self.titular} | Saldo: R${self.saldo:.2f}")


# Teste simples
if __name__ == "__main__":
    conta1 = ContaBancaria("Maria Silva")
    conta1.exibir_saldo()

    conta2 = ContaBancaria("João Souza")
    conta2.saldo = 150.75  # simulando alteração no saldo
    conta2.exibir_saldo()

