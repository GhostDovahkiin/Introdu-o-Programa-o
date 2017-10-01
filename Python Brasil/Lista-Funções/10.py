lista1 = []
lista2 = []
lista3 = []
for i in range(2):
    lista1.append(int(input("LISTA 1 \nDigite um número: ")))

for i in range(2):
    lista2.append(int(input("LISTA 2 \nDigite um número: ")))
lista3 = lista1 + lista2
print(lista3)
