qtd = int(input("Quantas peças há no estoque? "))
maiorv = 0
valios = 0
valort = 0
maiorpreco = 0
itemmaisvalios = 0
anomaisvalios = 0

for total in range(qtd):
    desc = str.lower(input("Qual o produto? "))
    valor = int(input("Qual o valor do produto? "))
    ano = int(input("Qual o ano do produto? "))

    if ano <= 1827:
        valios += 1      

    if valor > maiorv:
        maiorv = valor
        itemmaisvalios = desc
        anomaisvalios = ano
     
valort += valor
valorm = valort / qtd

print("Itens produzidos antes de 1827: {} \nValor médio dos itens: {} \nO item mais valioso é: {}, {}" .format(valios, valorm, itemmaisvalios, anomaisvalios))
    
