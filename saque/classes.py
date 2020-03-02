class Conta():
  saldo = 0

  def depositar(self, valor):
    self.saldo += valor

  def sacar(self, valor):
    if valor <= self.saldo:
      self.saldo -= valor
      print('Saque efetuado')
      self.consultar_saldo()
    else:
      print('Saldo insuficiente')

  def consultar_saldo(self):
    print(self.saldo)