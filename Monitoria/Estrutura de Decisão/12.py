valorh = float(input("Insira o valor de sua hora em R$: "))
hora = float(input("Digite a quantidade de horas trabalhadas: "))
salariob = valorh * hora

if salariob <= 900:
    ir = 0
    sindicato = salariob * 0.03
    fgts = salariob * 0.11

elif salariob <= 1500:
    ir = salariob * 0.05
    sindicato = salariob* 0.03
    fgts = salariob * 0.11

elif salariob <= 2500:
    ir = salariob * 0.10
    sindicato = salariob* 0.03
    fgts = salariob * 0.11

elif salariob > 2500:
    ir = salariob * 0.20
    sindicato = salariob* 0.03
    fgts = salariob * 0.11

else:
    print("Formato de inserção errado! \nTente novamente.")
descontos = ir + sindicato
salariol = salariob - ir - sindicato + fgts

print("Salario Bruto: ({} * {}) : R$ {:.2f}" .format(valorh, hora, salariob))
print("(-) IR (5%): R$ {:.2f}" .format(ir))
print("(-) Sindicato: R$ {:.2f}" .format(sindicato))
print("FGTS (11%): R$ {:.2f}" .format(fgts))
print("Total de descontos: R$ {:.2f}" .format(descontos))
print("Salário Líquido: R$ {:.2f}" .format(salariol))
    
    
