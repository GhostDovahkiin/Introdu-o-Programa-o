A = 80.000
AumentoA = 80.000 * 0.03
B = 200.000
AumentoB = 200000 * 0.015
ano = 0
while A < B:
    AumentoA = 80.000 * 0.03
    A = A + AumentoA
    ano += 1
print("Serão necessários {} ano(s)" .format(ano))
