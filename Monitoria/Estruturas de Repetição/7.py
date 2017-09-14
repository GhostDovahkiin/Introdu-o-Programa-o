# Faça um programa que leia 5 números e informe o maior número.
numM = 0
for i in range(5):
    num = int(input("Digite um número: "))
    if num > numM:
        numM = num
print("O maior número: {}" .format(numM))
