list = []
impar = []
par = []
for i in range(10):
	num = int(input("Digite um número: "))
	list.append(num)
	if num % 2 == 0:
		par.append(num)
	else:
		impar.append(num)
lista_ordenada = sorted(list)
impar_ordenada = sorted(impar)
par_ordenado = sorted(par)
print("List = ", lista_ordenada)
print("Impares = ", impar_ordenada)
print("Par = ", par_ordenado)
