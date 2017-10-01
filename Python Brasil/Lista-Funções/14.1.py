sim = 0
nao = 0
perguntas = []
for i in range(1):
    nome = str.upper(input("Digite seu nome: "))
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
    print("Voce {} foi classificado como suspeito".format(nome))
elif sim == 3 or sim == 4:
    print("Você {} foi classificado como cúmplice" .format(nome))
elif sim == 5:
    print("Você {} foi classificado como assassino" .format(nome))
else:
    print("Você {} foi classificado como inocente" .format(nome))
