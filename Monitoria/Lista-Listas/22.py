escolha = 1
defeito = [0]*4
porcentagem = [0]*4
cont = 0
print("Defeitos")
print("1-Necessita de esfera\n2-Necessita de limpeza\n3-Necessita troca do cabo ou conector\n4-Quebrado ou inutilizado")
while escolha !=0:
    escolha = int(input("Número do defeito: "))
    if escolha == 0:
        break
    elif escolha <= 4:
        defeito[escolha-1] += 1
    else:
        print("Defeito inválido")
    cont += 1
for i in range(len(defeito)):
    porcentagem[i] = defeito[i]/cont*100
print("Situação dos mouses")
print("{} mouses necessitam de esfera, tendo um percentual de {:.2f}%\n{} mouses precisam de limpeza, tendo um percentual de {:.2f}%".format(defeito[0], porcentagem[0], defeito[1], porcentagem[1]))
print("{} mouses precisam de troca de cabo ou conector, tendo um percentual de {:.2f}%\n{} mouses estão quebrados, tendo um percentual de {:.2f}%".format(defeito[2], porcentagem[2], defeito[3], porcentagem[3]))
