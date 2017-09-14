cont = 0
pessoas = int(input("Digite a quantidade de pessoas: "))
for i in range(pessoas):
    idade = int(input("Digite sua idade: "))
    cont += idade
    media = cont / pessoas

if media >= 0 and media <= 25:
    print("Turma jovem")
elif media >= 26 and media <= 60:
    print("Turma adulta")
else:
    print("Turma idosa")
