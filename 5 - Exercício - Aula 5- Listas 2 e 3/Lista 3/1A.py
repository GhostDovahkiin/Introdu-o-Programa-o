#CÓDIGO CERTO
rendaAnual = float (input())
if (rendaAnual <= 12000):
    imposto = 0
elif (rendaAnual > 60000):
    imposto = rendaAnual*0.07
else:
    imposto = rendaAnual*0.03
print(imposto)


#CÓDIGO ERRADO
rendaAnual = float (input())
if (rendaAnual <= 12000):
 imposto = 0
if (rendaAnual > 60000): # Redundância de IF deixa o código com a semântica errada. 
 imposto = rendaAnual*0.07
else:
 imposto = rendaAnual*0.03
print(imposto)
