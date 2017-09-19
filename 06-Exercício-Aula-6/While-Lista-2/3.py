# Programa para ler 20 números exibir a soma dos múltiplos de 3
n = 19
mult = 0
while n <=20:
    x = int(input("Digite um número: "))
    if (x % 3 == 0):
        mult = mult+x
    n += 1
print("A soma dos múltiplos de 3 resulta em: {}" .format(mult))
