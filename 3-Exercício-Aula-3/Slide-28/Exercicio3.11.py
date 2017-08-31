Mercadoria = float(input("Digite o valor da mercadoria: "))
Desconto = float(input("Digite o percentual de desconto: "))
Desconto = Desconto/100
Deconto = Desconto*10
NovoDesconto = (Mercadoria * Desconto) *-1 + Mercadoria
print("Seu desconto vai ser de: %2.4s" %Desconto)
print("Preço a pagar: %5.2f" %NovoDesconto)
