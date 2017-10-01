def validaDadosVoo(destino, turno):
    if destino == 'natal' and turno == 'diurno':
        valida = True
    elif destino == 'recife' and turno == 'diurno':
        valida = True
    elif destino == 'fortaleza' and turno == 'noturno':
        valida = True
    elif destino == 'recife' and turno == 'noturno':
        valida = True
    else:
        valida = False
    return valida

def calculaValorVoo(destino, turno):
    if destino == 'natal' and turno == 'diurno':
        preco = 80
    elif destino == 'recife' and turno == 'diurno':
        preco = 100
    elif destino == 'fortaleza' and turno == 'noturno':
        preco = 180
    else:
        preco = 90
    return preco
