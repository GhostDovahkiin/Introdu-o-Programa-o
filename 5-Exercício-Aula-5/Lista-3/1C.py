# CÓDIGO CERTO
a = int (input())
b = int (input())
c = int (input())
if (a > b) and (a > c):
    print(a)
elif (b > a) and (b > c):
    print(b)
else:
    print(c)


# CÓDIGO ERRADO
a = int (input())
b = int (input())
c = int (input())
if (a > b) and (a > c):
 print(a)
if (b > a) and (b > c):
 print(b)
if (c > a) and (c > b):
 print(c)
