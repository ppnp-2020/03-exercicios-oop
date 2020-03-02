from classes import Conta

conta_corrente = Conta()
conta_corrente.saldo = 200

conta_poupanca = Conta()
conta_poupanca.saldo = 5000

selecao = input('Selecione a conta desejada (1- corrente, 2- poupança): ')

if selecao != '1' and selecao != '2':
  print('Opção inválida')
else:
  if selecao == '1':
    conta_selecionada = conta_corrente
  else:
    conta_selecionada = conta_poupanca

  conta_selecionada.consultar_saldo()

  valor = float(input('Digite o valor para saque'))

  conta_selecionada.sacar(valor)