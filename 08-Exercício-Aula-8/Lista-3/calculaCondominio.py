def calculaCondominio(edificio, dias):
  valort = 0
  if edificio == 'duna':
    valort = ((dias*0.02) * 300) + 300
  elif edificio == 'chateau':
    valort = ((dias*0.04) * 450) + 450
  elif edificio == 'petit':
    valort = ((dias*0.03) * 220) + 220
  else:
    print("Nome de edifício inserido incorretamente")
  return valort

edificio = str.lower(input("Digite o nome do edifício: "))
dias = int(input("Digite os dias de atraso: "))

m =  calculaCondominio(edificio, dias)	
print("Total a ser pago: R${:.2f}" .format(m))
