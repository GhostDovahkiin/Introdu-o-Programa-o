# -*- coding: utf-8 -*-
velocidade = float(input("Qual a velocidade que o veículo estava? "))
if velocidade > 80:
    limite = velocidade-80
    multa = limite * 5
    print("Você ultrapassou os 80KM/H, sua multa é de %sR$" % (multa))
else:
    print("Você não ultrapassou o limite dos 80KM/H, parabéns!")