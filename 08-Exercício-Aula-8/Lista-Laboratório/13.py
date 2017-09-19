total2 = 0
cont = 0
contpeso = 0
import bibliotecacorreios

for i in range(50):
    tipoitem = str.lower(input("Digite o tipo de item: "))
    peso = float(input("Digite o peso do item(Kg): "))
    tamanho = str.lower(input("Digite o tamanho da embalagem: "))
    tipoentrega = str.lower(input("Digite o tipo de entrega: "))

    bibliotecacorreios.validaEntrega(tipoentrega)
    entrega = bibliotecacorreios.calcularCustoEntrega(tipoentrega)
    if tipoentrega == 'sedex':
        cont += 1

    bibliotecacorreios.validaPeso(peso)
    peso1 = bibliotecacorreios.convertePeso(peso)
    contpeso += peso1

    bibliotecacorreios.tipoItem(tipoitem)
    item= bibliotecacorreios.calculaCustoItem(tipoitem, peso1)

    bibliotecacorreios.validaEmbalagem(tamanho)
    tamanho1 = bibliotecacorreios.calculaCustoEmbalagem(tamanho)
    total1 = entrega + item + tamanho1
    total2 += total1

print("Peso total: {}g" .format(contpeso))
print("Quantidade de pedidos por SEDEX na semana: {}" .format(cont))
print('Custo total {} R$'.format(total2))
