# Programa para ler 25 números e
# exibir a quantidade de positivos e negativos
cont = 1
while (cont <= 5):
    numero = int(input("Digite um número: "))
    if (numero >= 0):
        qtdePositivos = numero
    else:
        qtdeNegativos = 0
        qtdeNegativos = numero * -1 
    cont += 1
print("A quantidade de positivos é: {} \nA quantidade de negativos é: {}".format(qtdePositivos, qtdeNegativos))
