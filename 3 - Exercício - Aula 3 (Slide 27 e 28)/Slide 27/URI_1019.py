A = float(input("Digite o tempo em segundos: "))
Horas = A // 3600
Minutos = A % 3600
Minutos = Minutos // 60
Segundos = Minutos % 60
print("%2.1s:%2.2s:%2.2s" %(Horas, Minutos, Segundos))
