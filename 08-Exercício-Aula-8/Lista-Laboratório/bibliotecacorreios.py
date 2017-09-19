Documento = 'documento'
Pacote = 'pacote'
Pequena = 'pequena'
Media = 'media'
Grande = 'grande'
Normal = 'normal'
Sedex = 'sedex'
Sedex10 = 'sedex10'

def tipoItem(tipoitem):
	if tipoitem == Pacote or tipoitem == Documento:
		return True
	else:
		return False

def validaPeso(peso):
	if peso >= 0:
		return True
	else:
		return False

def convertePeso(peso):
	peso *= 1000
	return peso

def calculaCustoItem(tipoitem ,  peso):
	if tipoitem == Documento:
		x = (2 * peso) / 1000
	else:
		x = (3 * peso) / 1000
	return x

def validaEmbalagem(tamanho):
	if tamanho == Pequena or tamanho == Media or tamanho == Grande :
		return True
	else:
		return False

def calculaCustoEmbalagem(tamanho):
	if tamanho == Pequena:
		custEmb = 4
	elif tamanho == Media:
		custEmb = 7
	elif tamanho == Grande:
		custEmb = 10
	else:
		custEmb = 0
	return custEmb

def validaEntrega(tipoentrega):
	if tipoentrega == Normal or tipoentrega == Sedex or tipoentrega == Sedex10:
		return True
	else:
		return False

def calcularCustoEntrega(tipoentrega):
	if tipoentrega == Normal:
		custEnt = 0
	elif tipoentrega == Sedex:
		custEnt = 5
	elif tipoentrega == Sedex10:
		custEnt = 8
	return custEnt
