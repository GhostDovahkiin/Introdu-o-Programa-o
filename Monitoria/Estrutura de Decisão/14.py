n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))
media = (n1 + n2) / 2
if media > 9.0 and media <= 10.0:
    print("Conceito A")
elif media > 7.5 and media <= 9.0:
    print("Conceito B")
elif media > 6.0 and media <= 7.5:
    print("Conceito C")
elif media > 4.0 and media <= 6.0:
    print("Conceito D")
elif media <= 4.0 and media == 0:
    print("Conceito E")
else:
    print("Média com valores sem conceito")
