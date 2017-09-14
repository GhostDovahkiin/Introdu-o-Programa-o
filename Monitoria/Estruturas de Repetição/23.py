numero = int(input('Digite um número: '))
x= 0
primo = 0
for i in range(1,numero+1):
    for f in range(1,i+1):
        if i % f == 0:
            x += 1
    if x == 2:
        primo += 1
    x = 0
print('Quandtidade de números primos: {}.'.format(primo))
