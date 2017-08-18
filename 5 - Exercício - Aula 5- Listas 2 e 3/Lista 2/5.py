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
else:
    print("Forma de pagamento inválida!")
    
    
