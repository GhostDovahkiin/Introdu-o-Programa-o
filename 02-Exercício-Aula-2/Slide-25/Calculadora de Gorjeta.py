refeicao = 44.50
imposto = 0.0675
gorjeta = 0.15


refeicao = refeicao + refeicao * gorjeta
total = refeicao + refeicao * gorjeta

print("O custo total de sua refeição é:%.2f" % total)
