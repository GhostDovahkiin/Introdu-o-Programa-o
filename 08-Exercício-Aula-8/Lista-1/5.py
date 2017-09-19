import liblista1
divisor = 300
cont = 0
cont1 = 0
for i in range(20):
    num = int(input("Digite um número. \nSerá testado se ele é multiplo de 4: "))
    mult = liblista1.testaMultiplo4(num)
    if mult == True:
        cont += 1

    soma = liblista1.testaDivisor(divisor, num)
    if soma == True:
         cont1 += num
print(" Há {} múltiplos de 4 \nA soma dos divisores de 300: {}" .format(cont, cont1))
