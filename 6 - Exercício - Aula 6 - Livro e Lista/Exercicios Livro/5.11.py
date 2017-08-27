depo_inicial = float(input("Insira o depósito inicial: "))
taxa_juros = float(input("Insira o juros:" ))
cont_meses = 0
jurosf = taxa_juros/100
jurospg = 0


while cont_meses < 24:
    cont_meses += 1
    taxa_mes = (depo_inicial * jurosf)
    taxa_final = taxa_mes + depo_inicial
    depo_inicial = taxa_final
    jurospg = jurospg + taxa_mes
    print("Taxa no mês {}: {:.2f}".format(cont_meses, taxa_final))
print("Taxa nos 24 meses: {:.2f}" .format(jurospg))
