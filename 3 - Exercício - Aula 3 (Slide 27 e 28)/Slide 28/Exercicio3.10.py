Salario = float(input("Digite seu salário: "))
Aumento = float(input("Digite o percentual de aumento: "))
Aumento = Aumento/100
NovoSalario = (Salario * Aumento) + Salario
print("Seu novo salário agora é: %5.2f" %NovoSalario)
