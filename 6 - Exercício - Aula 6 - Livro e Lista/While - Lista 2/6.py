total = 0
cont = 0
qtdade = int(input("Quantidade de filhos: "))
while (qtdade >= 0):
    total += qtdade
    cont += 1
    qtdade = int(input("Quantidade de filhos: "))
    media = total / cont
print("A média de filhos total é: {:.0f}" .format(media))
