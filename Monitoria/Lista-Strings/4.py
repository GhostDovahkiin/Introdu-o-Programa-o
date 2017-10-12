str = str.upper(input("Digite seu nome: "))
for i in range(len(str)):
	for a in range(i+1):
		print(str[a], end = ' ')
	print()
