import math
A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))
if (A != 0):
    delta = (B * B) - (4 * A * C)
    if (delta > 0):
        x1 = (-B + math.sqrt(delta)) / (2 * A)
        x2 = (-B - math.sqrt(delta)) / (2 * A)
        print("R1 = %.5f" % x1)
        print("R2 = %.5f" % x2)
    elif (delta < 0):
        print("Impossivel calcular")
else:
    print("Impossivel calcular")
