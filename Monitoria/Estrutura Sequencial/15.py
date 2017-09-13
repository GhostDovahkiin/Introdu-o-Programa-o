ganho = float(input("Digite seu ganho por hora: "))
horas = int(input("Digite o número de horas: "))
st = ganho * horas
ir = st * 0.11
inss = st * 0.08
sindicato = st * 0.05
sl = st - ir - inss - sindicato
print( "Salario Bruto: {:.2f}R$" .format(st))
print("IR (11%): {:.2f}R$" .format(ir))
print('INSS (8%): {:.2f}R$' .format(inss))
print("Sindicato (5%): {:.2f}R$" .format(sindicato))
print("Salário Líquido: {:.2f}R$" .format(sl))
