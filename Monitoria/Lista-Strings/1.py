print("Compara duas strings")
str1 = input("Frase 1: ")
str2 = input("Frase 2: ")
print("Comprimento String 1: {}" .format(len(str1)))
print("Comprimento String 2: {}" .format(len(str2)))
if len(str1) == len(str2):
	print("As duas strings são iguais")
else:
	print("As duas strings são diferentes")
if str1 == str2:
	print("As duas strings possuem conteúdos iguais")
else:
	print("As duas strings possuem conteúdos diferentes") 
