import FlyLib
sim = 'sim'
totalrecife = 0
valor = []
for i in range(5):
    while sim == 'sim':
        dest = str.lower(input("Digite seu destino: "))
        turn = str.lower(input('Digite seu turno: '))
        d = FlyLib.validaDadosVoo(dest, turn)
        if d == True:
            v = FlyLib.calculaValorVoo(dest, turn)
            valor.append (FlyLib.calculaValorVoo(dest, turn))
            if dest == 'recife':
                totalrecife  += v
        else:
            print("Destino ou turno inseridos incorretamente.")
            sim = str.lower(input("Deseja inserir os dados novamente? "))
        sim = str.lower(input("Deseja inserir mais dados? "))
print("Valores pagos: R${}" .format(valor))
print("Valor pago em passagens para Recife: R${}" .format(totalrecife))

            
