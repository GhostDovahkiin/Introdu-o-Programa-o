altura = float(input("Digite sua altura: "))
sexo = str.lower(input("Digite seu sexo: "))
if sexo == 'masculino':
    imc = (72.7*altura) - 58
else:
    imc = (62.1*altura) - 44.7
print("Seu peso ideal é: {:.2f}" .format(imc))
peso = float(input("Digite seu peso: "))
if peso > imc:
    print("Você está acima do peso ideal!")
else:
    print("Você está abaixo do peso ideal!")
