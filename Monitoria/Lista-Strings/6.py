dia, mes, ano = map(str,input("Digite o dia, mês e ano de nascimento. \nExemplo: (xx/xx/xxxx)\n ----> ").split("/"))
meses = [" ", "janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
mes = meses[int(mes)]
print("Você nasceu em {} de {} de {}" .format(dia, mes, ano))


