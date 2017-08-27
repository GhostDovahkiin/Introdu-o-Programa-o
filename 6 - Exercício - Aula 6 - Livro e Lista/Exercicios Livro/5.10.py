pontos = 0
questao = 1
while questao <= 3:
    resposta = str.lower(input("Resposta da questão {}: " .format(questao)))
    if questao == 1 and  resposta == "b":
        pontos = pontos + 1
    if questao == 2 and resposta == "a":
        pontos = pontos + 1
    if questao == 3 and resposta =="d":
        pontos = pontos + 1
    questao += 1
print("O aluno fez {} ponto(s)" .format(pontos))
