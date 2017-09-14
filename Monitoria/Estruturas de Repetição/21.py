num = int(input("Digite um número: "))
cont = 0
for i in range(1,num+1):
    if (num % i) == 0:
        cont += 1
if cont == 2:
    print("{} é primo" .format(num))
else:
    print("{} não é primo" .format(num))
