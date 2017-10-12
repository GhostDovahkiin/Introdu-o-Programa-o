def ex01(num):
	for i in range(num):
  		var = ""
  		for d in range(i + 1):
    			var += str(i + 1) + " "
  	return var

def ex02(num):
  for i in range(num):
  	var = ""
  	for i in range(i + 1):
    		var += str(i + 1) + " "
  	return var

def ex03(num1, num2, num3):
  soma = num1 + num2 + num3
return soma

def ex04(num):
  if num > 0:
    return "P"
  else:
    return 'N'

def ex05(porc, cust):
  juros = (porc * cust) / 100
  cust1 = cust + juros
return cust1

def ex06(horas):
  if horas > 12:
    horas = horas - 12
    fuso = 'P.M'
  else:
    fuso = 'A.M'
return("Hora convertida: {}:{} {}" .format(horas, minutos, fuso))

def ex07(valor, dias):
	if dias == 0:
		print(valor)
	else:
  		prestação = valor * dias
		multa = prestação * 0.03 
		juros = multa*(dias * 0.1/100)
  	return("Valor a ser pago: {:.2f}R$" .format(prestação+juros))

def ex08(num)
	return len(str(num))

def ex09(num):
	return num[::-1]

def ex10(dado):
	if dado == 7 or dado == 11:
		print('Você ganhou!')
	elif dado == 2 or dado == 3 or dado == 12:
		print('Craps!')
	else:
		from random import randint
		if dado == 7 or dado == 11:
			print("Você ganhou!")
		elif dado == 2 or dado == 3 or dado == 12:
			print("Craps! Você perdeu!")
		else:
			while dado != 7:
				novo = randit(2, 12)
				while novo != dado:
					novo = randit(2, 12)
				print('Você ganhou')
				break
			print("Você perdeu")

def ex11(dia, mes, ano):
	meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'] 	
	if mes == 2 and dia <= 28:
		print("Data inválida")
	elif dia <= 31 and mes <= 12:
		print("{} de {} de {}" .format(dia, meses[mes-1], ano)
	else:
		print("NULL")
def ex12(string):
	import random
	s
	alo = "".join(random.sample(string)))
	return str.lower(alo) 


	
		
	
	





