setor = str.lower(input("Digite o tipo de setor escolhido: "))
ingresso = str.lower(input("Digite o tipo de ingresso: "))
if setor == 'platéia':
    if ingresso == 'inteira':
        valor = 350.0
        taxa = valor +(valor*0.05)
    else:
        print("Tipo de ingresso inválido")
        exit()
elif setor == 'cadeira':
    if ingresso == 'meia':
        valor = 200.0
        desconto = 200*0.05 + 200
        taxa = desconto * 0.5 + 5
    else:
        valor = 200.0
        taxa = valor+(valor*0.05)
elif setor == 'arquibancada':
    if ingresso == 'meia':
        valor = 100.0
        desconto = 100*0.05 + 100 + 5
        taxa = desconto * 0.5
    else:
        valor = 100.0
        taxa = valor+(valor*0.05)
else:
    print("Setor inválido")
    exit()
print("%2.2fR$" %(taxa))

    
    
    
    
