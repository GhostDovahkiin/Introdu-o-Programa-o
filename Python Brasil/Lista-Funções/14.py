sim = 0
nao = 0
perguntas = []
for i in range(1):
    perguntas.append(str.lower(input("A. Telefonou para a vítima? ")))
    perguntas.append(str.lower(input("B. Esteve no local do crime? ")))
    perguntas.append(str.lower(input("C. Mora perto da vítima? ")))
    perguntas.append(str.lower(input("D. Devia para a vítima? ")))
    perguntas.append(str.lower(input("E. Já trabalhou com a vítima? ")))
    for i in perguntas:
        if i == 'sim':
            sim += 1
        elif i == 'não':
            nao += 1
        else:
            print("Resposta incorreta")
            break
if sim == 2:
    print("O meliante é suspeito")
elif sim == 3 or sim == 4:
    print("O meliante é cúmplice")
elif sim == 5:
    print("Você é um asassino")
else:
    print("Você é inocente")
