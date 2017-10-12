carros = [['fusca',7,],['gol',10],['uno',12,5],['Vectra',9],['Peugeout',14.5]]
menor = 10000
print('Comparativo de Consumo de Combustivel')

for i in range(len(carros)):
	print(" ")
	print('Veiculo {}'.format(i+1))
	print('Nome: {}'.format(carros[i][0]))
	print('Km por litro: {}'.format(carros[i][1]))
print()

print('Relatorio Final\n')
for i in range(len(carros)):
	litro = 1000/carros[i][1]
	custo = litro*2.25
	if litro < menor:
		menor = litro
		nome = carros[i][0]
	print('{} -  {}	 -  {}  -  {:.2f}  Litros  -  R$  {:.2f}'.format(i+1,carros[i][0],carros[i][1],litro,custo))
print()

print('O menor consumo é do {}'.format(nome))
		
		













