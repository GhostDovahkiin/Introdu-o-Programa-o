def calculaCondominio(edificio, dias):
  if edificio == 'duna':
    valort = 300 + (0.02 * dias)
  elif edificio == 'chateau':
    valort = 450 + (0.04 * dias)
  elif edificio == 'petit':
    valort = 220 + (0.03 * dias)
  else:
    print("Nome de edifício inserido incorretamente")
  return valort

edificio = str.lower(input("Digite o nome do edifício: "))
dias = int(input("Digite os dias de atraso: "))

m =  calculaCondominio(edificio, dias)	
print(m)
