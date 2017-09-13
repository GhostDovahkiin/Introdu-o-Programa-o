lado1 = float(input("Primeiro Lado: "))
lado2 = float(input("Segundo Lado: "))
lado3 = float(input("Terceiro Lado: "))

if (lado1+lado2 > lado3 or lado3+lado1 > lado2 or lado3+ladob2 > lado1):
    if lado1 == lado2 and lado1 == lado3 and lado1 == lado3:
        print("Triângulo Equilátero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Triângulo Isóceles")
    else:
        print("Triângulo Escaleno")
else:
    print("Não é um triângulo")
