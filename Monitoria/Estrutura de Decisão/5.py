n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1+n2) / 2
if media == 10:
    print("Aprovado com distinção")
elif media >= 7:
    print('Aprovado')
else:
    print('Reprovado')
