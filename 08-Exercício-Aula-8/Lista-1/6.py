import liblista1
num1 = 0
for i in range(5):
    num = int(input("Digite um número: "))
    maiornum = liblista1.calculaMaior(num, num1)
    num1 = maiornum
print("O maior número é: {}" .format(num1))
