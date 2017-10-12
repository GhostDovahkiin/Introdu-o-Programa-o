frase = str.lower(input("Digite uma frase: "))
espaco = 0
vogal = 0
for i in frase:
	if i == " ":
		espaco += 1
	elif i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
		 vogal += 1
print("Quantidade de espaços: {}" .format(espaco))
print("Quantidade de vogais: {}" .format(vogal))

