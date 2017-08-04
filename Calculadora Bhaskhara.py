############ Calculadora de Bhaskhara ############
from math import sqrt
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))
x = (b**2)-(4*a*c)

if x < 0 :
x = math.sqrt(x)
x = (-b+x)/(2*a)
print("O valor de X é %s" %(x))

else:
x = math.sqrt(x)
xi = (-b+x)/(2*a)
xii = (-b+x)/(2*a)
print("O valor de X1 é %s, e X2 é %s" %(x1, x2))

