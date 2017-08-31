# -*- coding: utf-8 -*-
salario = float(input("Qual o valor de seu salário? "))
if salario > 1.250:
    aumento = salario * 0.1 + salario
elif salario <= 1.250:
    aumento = salario * 0.15 + salario

print("Seu novo salário é: %s" % (aumento))
