A = float(input("Digite o tempo em segundos: "))
Horas = A / 3600
Minutos = A % 3600
Minutos = Minutos / 60
Segundos = Minutos % 60
print("O tempo de duração foi %2.1s hora(s), %2.2s minuto(s) e %2.2s segundos(s)" %(Horas, Minutos, Segundos))
