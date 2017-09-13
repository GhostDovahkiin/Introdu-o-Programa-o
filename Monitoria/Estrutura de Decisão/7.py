# Faça um Programa que leia três números e mostre o maior e o menor deles
num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
num3 = int(input("Digite um número: "))
maxi = 0
mini = 0

if num1 > num2 and num1 > num3:
    maxi = num1
elif num2 > num1 and num2 > num3:
    maxi = num2
else:
    maxi = num3

if num1 < num2 and num1 < num3:
    mini = num1
elif num2 < num1 and num2 < num3:
    mini = num2
else:
    mini = num3

print("O maior número é {}" .format(maxi))
print("O menor número é {}" .format(mini))
