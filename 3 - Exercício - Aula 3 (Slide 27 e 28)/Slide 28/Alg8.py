Dias1 = int(input("Digite sua idade total em dias: "))
Anos = Dias1 / 365
Meses = Dias1 % 365 / 30
Dias = Dias1 % 365
print ("Você tem %2.2s Ano(s), %2.2s mes(es) e %2.1s dia(s)" %(Anos, Meses, Dias))
