salario_antigo = float(input("Digite seu salário: "))

if salario_antigo <= 280:
    aumento = 0.2 * salario_antigo
    tela = 'Seu aumento é de 20%'

elif salario_antigo <= 700 and salario_antigo >= 280:
    aumento = 0.15 * salario_antigo
    tela = 'Seu aumento é de 15%'

elif salario_antigo <= 1500 and salario_antigo >= 700:
    aumento = 0.10 * salario_antigo
    tela = 'Seu aumento é de 10%'

else:
    aumento = 0.05 * salario_antigo
    tela = 'Seu aumento é de 5%'
salario_novo = aumento + salario_antigo
    

print("Seu salario antes do reajuste: R$ {:.2f}" .format(salario_antigo))
print(tela)
print("Seu aumento é de R$ {:.2f}" .format(aumento))
print("Seu novo salário é: R$ {:.2f}" .format(salario_novo))


