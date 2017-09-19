import bibliotecacorreios

tipoitem = str.lower(input("Digite o tipo de item: "))
peso = float(input("Digite o peso do item(Kg): "))
tamanho = str.lower(input("Digite o tamanho da embalagem: "))
tipoentrega = str.lower(input("Digite o tipo de entrega: "))

bibliotecacorreios.validaEntrega(tipoentrega)
entrega = bibliotecacorreios.calcularCustoEntrega(tipoentrega)

bibliotecacorreios.validaPeso(peso)
peso1 = bibliotecacorreios.convertePeso(peso)

bibliotecacorreios.tipoItem(tipoitem)
item= bibliotecacorreios.calculaCustoItem(tipoitem, peso1)


bibliotecacorreios.validaEmbalagem(tamanho)
tamanho1 = bibliotecacorreios.calculaCustoEmbalagem(tamanho)

print('Custo total {} R$'.format(entrega+item+tamanho1))
