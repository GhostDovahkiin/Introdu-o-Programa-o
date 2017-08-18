numero = float(input("Digite um número:"))
if numero % 2 == 0:
    res = "Par"
elif numero % 2 > 0:
    res = "Ímpar"
else:
    res = "ERRO!"
print(res)