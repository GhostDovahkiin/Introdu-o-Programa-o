import AbadaLib
vendidos = []
total = []
for i in range(100):
    qtd = int(input("Digite a quantidade de peças(Abadás) vendidos: "))
    comissao = AbadaLib.calculaComissao(qtd)
    bonus = AbadaLib.calculaBonus(qtd)
    vendidos.append(comissao+bonus)
    total.append(qtd)
for i in range(5):
    print("\n\nTotal de peças vendidas: {} \nSua comissão é de: R${:.2f}" .format(total[i], vendidos[i]))
