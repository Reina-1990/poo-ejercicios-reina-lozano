#Cuenta bancaria
class CuentaBancaria:
    def __init__(self):
        self.saldo = 0

    def depositar(self, monto):
        self.saldo += monto
        print("Depósito realizado. Saldo actual:", self.saldo)

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            print("Retiro realizado. Saldo actual:", self.saldo)
        else:
            print("Fondos insuficientes")


# cuenta
cuenta = CuentaBancaria()

# métodos
cuenta.depositar(100)
cuenta.retirar(50)
cuenta.retirar(100)