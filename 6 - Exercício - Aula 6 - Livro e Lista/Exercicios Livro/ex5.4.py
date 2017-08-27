#Imprimir números ímpares, sendo que o Y o usuário insira

x2 = int(input("Digite um número: "))
x = 1
print(x)
while x <= x2:
    if x % 3 == 0:
        print(x)
    x += 1
