def calculaEstacionamento (veiculo, horas, minutos):
  if horas > 1 and horas <= 5:

    if minutos == 0:
        total = 3

  else:
      total = (horas - 5)*2 + 3

  if veiculo == 'moto':
    total = total / 2
  return total 


veiculo = str.lower(input("Digite o tipo de veículo: "))
hora = int(input("Digite a quantidade de horas: "))
minuto = int(input("Digite a quantidade de minutos: "))

total = calculaEstacionamento(veiculo,hora,minuto)
print("Taxa a ser paga: R${}" .format(total))
