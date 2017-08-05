Kms = int(input("Quantos KM você percorreu? "))
Dias = int(input("Quantos dias você usou o carro? "))
KM_RODADO = Kms * 0.15
Diaria = Dias * 60
Total = KM_RODADO + Diaria
print("Você andou %sKm(s) em %sdia(s), e terá de pagar %5.4sR$" %(Kms, Dias, Total))
