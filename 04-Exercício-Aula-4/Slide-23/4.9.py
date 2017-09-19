# -*- coding: utf-8 -*-
valor = float(input("Insira o valor da casa: "))
salario = float(input("Insira seu salário:"))
anos = int(input("Em quantos anos pretende pagar? "))
cond = salario * 0.30
prestacao = valor / (anos/12)
if prestacao > cond:
    print("Você não foi qualificado para o empréstimo!")
elif prestacao < cond:
    print("Parabéns, você foi qualificado para o empréstimo!")
