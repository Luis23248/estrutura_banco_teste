class Conta:
    def __init__(self, numero_conta: int, agencia:int) -> None:
        self._numero_conta = numero_conta
        self._agencia = agencia
        self._valor = 0

    def depositar(self, valor):
        if valor < 0:
            self._saldo = 0
        else:
            self._saldo += valor
    def sacar(self, valor):
        self._valor -= valor

