peso = float(input("Digite a quantidade de quilos: "))
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
else:
    excesso = 0
    multa = 0
print("Quilos excedentes: {}" .format(excesso))
print("Multa a pagar: {:.2f}" .format(multa))
