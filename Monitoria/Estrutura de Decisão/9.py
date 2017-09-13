# Faça um Programa que leia três números e mostre-os em ordem decrescente.
num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
num3 = int(input("Digite um número: "))

if num2 > num1:
    num1,num2 = num2,num1

if num3 > num1:
    num1,num3 = num3,num1

if num3 > num2:
    num2,num3 = num3,num2

print("{} > {} > {}" .format(num1, num2, num3))
