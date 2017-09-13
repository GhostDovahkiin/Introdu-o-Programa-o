qtd = int(input("Digite a quantidade de vendas: "))
qMarfim, qBranco = 0, 0
qBrastemp, qElectrolux = 0, 0
qtdMoveis, qtdDecor, qtdEletro = 0, 0, 0
qMoveis, qDecor, qEletro = 0, 0, 0
total = 0

for i in range(qtd):
    tipo = str.lower(input("Digite o tipo de produto: "))

    if tipo == 'móvel':
        qMoveis += 1
        cor = str.lower(input("Digite a cor: "))
        if cor == 'marfim':
            qMarfim+= 1
        elif cor == 'branco':
            qBranco += 1
        else:
            print("Cor inválida")
        pctMarfim = (qMarfim / qMoveis) * 100
        pctBranco = (qBranco / qMoveis) * 100

        
    elif tipo == 'eletrodoméstico':
        qEletro += 1
        marca = str.lower(input("Digite a marca: "))

        if marca == 'brastemp':
            qBrastemp += 1
        elif marca == 'electrolux':
            qElectrolux += 1
        else:
            print("Marca inválida")
        pctElectrolux = (qElectrolux / qEletro) * 100
        pctBrastemp = (qBrastemp / qEletro) * 100


    elif tipo == 'decoração':
        qDecor += 1
        preço = float(input("Digite o preço: "))
        pctPreco += preco


if qMoveis > 0 and qEletro == 0 and qDecor == 0:
    print("Percentuais --> {}% Marfim, {}% Branco" .format(pctMarfim, pctBranco))

elif qEletro > 0 and qMoveis == 0 and qDecor == 0:
    if qBrastemp > qElectrolux or qElectrolux > qBrastemp:
        print("Percentuais --> {}% Electrolux, {}% Brastemp" .format(pctElectrolux, pctBrastemp))
    elif qElectrolux == qBrastemp:
        print("As duas marcas foram igualmente vendidas")

elif qDecr > 0 and qEletro == 0 and qMoveis == 0:
    print("Preço médio de decoração: {:.2}R$" .format(pctPreco / qDecor))
    print("Nenhum móvel foi vendido ou eletrodoméstico")


        
