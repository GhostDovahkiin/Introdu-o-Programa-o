# -*- coding: utf-8 -*-
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = input("Qual operação desejada? Digite somente o símbolo da operação")
if operacao == "+":
    res = numero1 + numero2
elif operacao == "-":
    res = numero1 - numero2
elif operacao == "/":
    res = numero1 / numero2
elif operacao == "*":
    res = numero1 * numero2
else:
    print("Operação não especificada. \nDigite um destes símbolos para proseguir(+, -, *, /")
print("O resultado: ", res)