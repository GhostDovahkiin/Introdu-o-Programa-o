lista = [[200,299],[300,399],[400,499],[500,599],[600,699],[700,799],[800,899],[900,999],[1000]]
qtdvendas = [0,0,0,0,0,0,0,0,0]
vendedor = int(input("Quantidade de vendedores: "))
for i in range(vendedor):
	salariob = float(input("Digite seu ganho bruto: "))
	salario = 200 + (0.09 * salariob)
	if salario < 1000:
	
		for i in range(len(lista)):
			if salario >= lista[i][0] and salario <= lista[i][1]:
				qtdvendas[i]+= 1
	else:
		qtdvendas[8] += 1
print("Lista de resultado de vendedores: {}" .format(qtdvendas))

