cpvan = 20
cpbus = 40
qtdade = int(input())
total = qtdade

nbus = qtdade//cpbus
qtdade = qtdade%cpbus
nvans = qtdade//cpvan
qtdade = qtdade%nvans
if (qtdade>0):
    nvans += 1
print(' %d onibus e %d vans')
valor = ((nbus*350) + (nvans*200)//total)
