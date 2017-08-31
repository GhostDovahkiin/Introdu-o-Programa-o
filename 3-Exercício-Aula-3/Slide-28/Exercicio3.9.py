Dia = int(input("Digite uma quantidade de dias: "))
Hora = int(input("Digite uma quantidade de horas: "))
Minuto = int(input("Digite uma quantidade de minutos: "))
Segundo = int(input("Digite uma quantidade de segundos: "))
SegundoTotal = (Dia*24*60*60) + (Hora*60*60) + (Minuto*60) + Segundo
print("%fs" %SegundoTotal)

