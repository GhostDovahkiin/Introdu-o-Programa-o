# -*- coding: utf-8 -*-
kw = int(input("Insira a quantidade de kWh: "))
inst = str.lower(input("Insira o tipo da sua instalação: "))
if inst == "residencial":
    if kw <= 500:
        preco = kw * 0.40
    else:
        preco = kw * 0.65
elif inst == "comercial":
    if kw <= 1000:
        preco = kw * 0.55
    else:
        preco = kw * 0.60
elif inst == "industrial":
    if kw <= 5000:
        preco = kw * 0.55
    else:
        preco = kw * 0.60
print("O valor a pagar é R$",preco)
