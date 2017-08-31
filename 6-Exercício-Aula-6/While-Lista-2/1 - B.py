# Programa para ler 30 números e
# exibir a quantidade de positivos
cont = 1
qtdePositivos = 0
while (cont <= 30):
    numero = int(input("Digite um número: "))
    if (numero >= 0):
        qtdePositivos = numero
    cont += 1
print("A quantidade de positivos é: {}".format(qtdePositivos))
