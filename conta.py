# conta.py

class ContaBancaria:
    """
    Representa uma conta bancária simples.
    """
    def __init__(self, titular):
        """
        Inicializa a conta com um titular e saldo inicial de 0.
        """
        self.titular = titular
        self.saldo = 0.0 # O saldo inicia em 0

    def exibir_saldo(self):
        """
        Exibe o nome do titular e o saldo atual da conta.
        """
        print(f"Titular: {self.titular}")
        print(f"Saldo: R$ {self.saldo:.2f}")

# --- Teste Simples ---
if __name__ == '__main__':
    # 1. Cria uma nova conta bancária (substitua GUSTAVO)
    minha_conta = ContaBancaria("GUSTAVO")

    # 2. Exibe o saldo inicial
    print("--- Teste de Exibição de Saldo ---")
    minha_conta.exibir_saldo()
    print("---------------------------------")

