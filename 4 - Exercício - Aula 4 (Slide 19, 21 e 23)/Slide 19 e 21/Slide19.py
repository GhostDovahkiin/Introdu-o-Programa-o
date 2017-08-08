# -*- coding: utf-8 -*-
salario = float(input("Digite seu salário: "))
if salario > 1000:
    imposto1 = 0.17 * salario
    print("Seu salário é maior que 1000,00R$, então seu imposto será: %s" %(imposto1))
else:
    imposto2 = 0.08 * salario
    print("Seu salário é menor ou igual a 1000,00R$, então você pagará: %s" %(imposto2))
