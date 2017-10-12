media = []
maiorq = 0
for i in range(2):
	nota=0
	for i in range(4):
		nota += float(input("Digite sua nota: "))
	media.append(nota/4)
for i in media:
	if i >= 7:
		maiorq += 1
print("{} Aluno(s) tiveram notas acima ou na média" .format(maiorq))
		
