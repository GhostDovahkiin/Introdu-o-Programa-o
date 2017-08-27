# Programa para ler varios numeros, e exibir a média dos pares
n = 0
pares = 0
media = 0
n1 = 0
while n < 100:
    n = int(input("Digite um número: "))
    if n % 2 == 0:
        n+= 1
        n1 += n 
        media = n1 / n
print("A média dos números pares é: {:.2f} ".format(media))
