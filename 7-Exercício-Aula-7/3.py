qtd = 0
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
if num1 > num2:
    num1, num2 = num2, num1
for i in range(num1+1,num2):
    if i % 4 == 0:
        qtd += 1
print("{} múltiplos" .format(qtd))
    
    
    
