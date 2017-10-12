nome = str.upper(input("Digite seu nome: "))
res = 0
print(nome, end = "")
for i in range(len(nome)):
    print(nome[:-res])
    res += 1

