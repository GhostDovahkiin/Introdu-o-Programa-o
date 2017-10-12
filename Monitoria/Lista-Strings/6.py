dia, mes, ano = map(str,input(":").split("/"))
meses = [" ", "janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
mes = meses[int(mes)]
print("Você nasceu em {} de {} de {}" .format(dia, mes, ano))


