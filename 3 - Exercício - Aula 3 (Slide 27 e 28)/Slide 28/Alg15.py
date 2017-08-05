Dinheiro = int(input("Digite o valor em R$: "))
Nota100 = Dinheiro/100
Dinheiro = Nota100 % 100
Nota50 = Dinheiro /50
Dinheiro = Nota50 % 50
Nota10 = Dinheiro/10
Dinheiro = Nota10 % 10
Nota5 = Dinheiro/5
Dinheiro = Nota5 % 5
Nota1 = Dinheiro/1
print("Seu dinheiro decomposto é Notas de 100 = %2.1s. \nNotas de 50 = %2.2s. \nNotas de 10 = %2.2s. \nNotas de 5 = %2.2s. \nNotas de 1 = %2.2s" %(Nota100, Nota50, Nota10, Nota5, Nota1))

