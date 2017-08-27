# Programa para ler 20 números e
# exibir a soma dos pares
n = 1
soma = 0
while n <= 20:
    x = int(input("Digite um número: "))
    if (x % 2 == 0):
        soma = soma + x
    n += 1
print("A soma dos pares resulta em: {}" .format(soma))
