import Q1lib
print('BAIRRO OCEANIA')

edificio = str.lower(input("Digite o nome do edifício: "))
dias = int(input("Digite os dias de atraso: "))
m = Q1lib.calculaCondominio(edificio, dias)	
print(m)




