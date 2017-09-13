metros= int(input("Quantidade da area a ser pintada em m²: "))
litro = metros / 6
total_litro = litro + litro/10
total_latas = total_litro//18
total_galao2 = 0
total_galao = 0
total_galao1 = 0

if total_latas > 0:
    total_galao = total_litro%18
    if total_galao % 3.6 > 0:
        total_galao1 = total_galao // 3.6
        total_galao2 = total_galao1 + 1
        if total_galao2 > 3:
            total_galao = 0
            total_latas += 1

preco_lata = total_latas*25
preco_galao = total_galao2*80

print("Quantidade de litros necessaria: {:.2f}" .format(total_litro))
print("Total de latas: {:.2f}" .format(total_latas))
print("Total de galões: {:.2f}" .format(total_galao))
print("Preço total em latas: R${:.2f}" .format(preco_lata))
if total_galao != 0:
    print("Preço total em galoes: R${:.2f}" .format(preco_galao))
            



