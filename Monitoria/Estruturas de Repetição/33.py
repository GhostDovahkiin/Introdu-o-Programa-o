temp = float(input("Digite a temperatura: "))
adc = 'sim'
maiortemp = 0
menortemp = 0
while adc == 'sim':
    temp = float(input('Digite a temperatura: '))
    med +=1
    tempT += temp
    adc = str.lower(input('Adicionar mais temperaturas? '))
    
    if temp > maiortemp:
        maiortemp = temp
    if temp < menortemp:
        menortemp = temp
media = tempT / med
print("Maior temperatura: {}" .format(maiortemp))
print("Menor temperatura: {}" .format(menortemp))
print("Media das temperaturas: {}" .format(media))
    
