letra = str.lower(input("Digite uma letra ou palavra: "))
def posicoesQueIniciamCom(lista, letr = letra):
    word = []
    for i, palavra in enumerate(lista):
        if palavra.startswith(letra):
           word.append(i)
    return word

nomes = []

for i in range(3):
  nomes.append(str.lower(input("Digite uma palavra: ")))
print (posicoesQueIniciamCom(nomes))
