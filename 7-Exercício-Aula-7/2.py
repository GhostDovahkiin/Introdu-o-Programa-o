pedidos = 50
pedido = 0
pt = 0
for total in range(pedidos):
    tipocob = str.lower(input("Digite o tipo de cobrança. \nPeça ou Peso? "))

    if tipocob == 'peça':
        qtd1 = int(input("Digite a quantidade de peças: "))
        taxa = qtd1 * 7
        
    elif tipocob == 'peso':
        qtd2 = int(input("Digite a quantidade de Quilos: "))
        taxa = qtd2 * 5

    lavage = str.lower(input("Lavagem a seco? "))
    if lavage == 'sim':
        taxa += 3.50
        secoqtd += 1
    else:
        secoqtd = 0
    pt += taxa
    pedido += 1

    print("Valor do {}º pedido: {} \nTotal arrecadado: {} \nQuantidade de lavagens a seco: {}" .format(pedido, taxa, pt, secoqtd))
    
