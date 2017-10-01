lista = []
valor = 0
menos7 = 0
cont = 0
nota = (int(input("Digite sua nota: "))
while nota != -1:
    lista.append(nota)
    valor+= 1
    soma += nota
    nota = (int(input("Digite sua nota: "))
media = soma / valor
for i in lista:
    if i > media:
        cont+= 1

    if media < i:
        menos7 += 1
    
    
    
