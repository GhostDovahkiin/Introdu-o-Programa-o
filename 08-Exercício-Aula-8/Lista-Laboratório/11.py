total2 = 0
import bibliotecacorreios

for i in range(50):
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
    total1 = entrega + item + tamanho1
    total2 += total1

print('Custo total {} R$'.format(total2))
