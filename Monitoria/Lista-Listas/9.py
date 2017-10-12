A = []
B = []
for i in range(10):
	num = int(input("Digite um número: "))
	A.append(num)
	B1 = num**2
	B.append(B1)
print("A Soma dos quadrados dos números: {}" .format(sum(B)))
