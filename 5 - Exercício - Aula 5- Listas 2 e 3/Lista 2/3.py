num1 = float(input("Digite um número: "))
num2 = float(input("Digite um número: "))
num3 = float(input("Digite um número: "))
if num1 > num2 and num3:
    res = num1
elif num2 > num1 and num3:
    res = num2
else:
    res = num3

print("O maior número é %2.1f" %(res))
