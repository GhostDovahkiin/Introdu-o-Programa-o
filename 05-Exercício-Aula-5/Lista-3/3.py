cpBus = 42
vlBus = 350
cpVan = 20
vlVan = 200

pessoas = int(input("Digite o número de pessoas: "))
totalpessoas = pessoas
nBus = pessoas // cpBus
pessoas = pessoas % cpBus
nVan = pessoas // cpVan
pessoas = pessoas % cpVan

if pessoas > 0:
    nVan += 1

print("{} onibus e {} vans" .format(nBus, nVan))

vTotal = ((nBus*vlBus)+(nVan*vlVan))/totalpessoas
print("R$ {:.2f} por pessoa" .format(vTotal))
