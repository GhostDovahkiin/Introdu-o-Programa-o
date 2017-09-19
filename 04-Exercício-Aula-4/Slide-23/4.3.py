# -*- coding: utf-8 -*-
A = float(input("Digite um número: "))
B = float(input("Digite um número: "))
C = float(input("Digite um número: "))
if A>B>C:
    print(A,C)
elif A>C>B:
    print(A,B)
elif B>A>C:
    print(B,C)
elif B>C>A:
    print(B,A)
elif C>A>B:
    print(C,B)
elif C>B>A:
    print(C,A)
