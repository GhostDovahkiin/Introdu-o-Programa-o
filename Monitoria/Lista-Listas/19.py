lista = [0]*6
med = [0]*6
soma = 0
while True:
	print("Qual o melhor sistema operacional para uso em servidores?")
	print("As principais respostas são:")
	print("1- Windowns Server\n2 - Unix\n3 - Linux\n4 - Netware\n5 - Mac OS\n6 - Outro")
	option=int(input(": ") )
	if option == 0:
		print('Invalido, Tente novamente!')
		break
	else:
		lista[option-1] += 1
		soma+=1
for i in range(len(lista)):
	med[i] = lista[i]/soma*100
print('Sistema Operacional	Votos	%')
print('------------------      ------  ---')
print('Windowns Server		{}	{:.2f}'.format(lista[0],med[0]))
print('Unix			{}	{:.2f}'.format(lista[1],med[1]))
print('Linux			{}	{:.2f}'.format(lista[2],med[2]))
print('Netware			{}	{:.2f}'.format(lista[3],med[3]))
print('Mac OS			{}	{:.2f}'.format(lista[4],med[4]))
print('Outro			{}	{:.2f}'.format(lista[5],med[5]))
print('------------------		--')
print('Total			{}'.format(soma))

