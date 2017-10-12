lista = list(range(20))
A = []
B = []
C = []
print('Lista A')
for i in range(len(lista)):
	num = int(input('Digite um inteiro: '))
	A.extend([num])

print('Lista B')
for i in range(len(lista)):
	num2 = int(input('Digite um inteiro: '))
	B.append(num2)
v=[]
for i in range(20):
  C = str(A[i]) + " " + str(B[i])
  v.append(C)
print(v)
