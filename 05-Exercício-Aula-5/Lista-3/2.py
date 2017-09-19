gasolina  = 2.53
etanol = 2.09
diesel = 1.92
tipo = str.lower(input("Digite o tipo do combustível: "))
quant = int(input("Digite a quantidade em R$ que deseja gastar: "))
if tipo == 'gasolina':
    litros = quant / gasolina
    print("Não ganhou troca de óleo")
elif tipo == 'etanol':
          litros = quant / gasolina
          if litros > 30:
              print("Você ganhou uma troca de óleo")
          else:
              print("Não ganhou troca de óleo")
else:
    litros = quant / diesel
    print("Não ganhou troca de óleo")
print("Litros ---> %2.2f" %(litros))
          
