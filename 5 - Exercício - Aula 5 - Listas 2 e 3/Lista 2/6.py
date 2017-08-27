valor = float(input("Digite o valor: "))
forma = str.lower(input("Digite a forma de pagamento: "))
if valor >= 100 and forma == 'dinheiro':
    desconto = valor - (valor * 0.10)
    print("Seu desconto é de %2.2fR$" %(desconto))
elif forma == 'cheque':
    desconto = valor
    print("Você não tem desconto. Total = %2.2fR$" %(valor))
elif valor < 100  and forma == 'dinheiro':
    desconto = valor
    print("Você não tem desconto. Total = %2.2fR$" %(valor))
elif forma == 'cartão':
    opcao = str.lower(input("Crédito ou Débito:"))
    if opcao == 'crédito':
        parcela = int(input("Digite o número de parcela: "))
        parcelamento = valor / parcela
        print("Serão {} parcelas de {}" .format(parcela, parcelamento))
        if parcela > 3:
            print("Você não pode parcelar mais de 3 vezes!")
    else:
        print("Você não pode parcelar. Valor total = {}R$" .format(valor))
