km = float(input("Quantos KM você pretende percorrer?"))
if km <= 200:
    passagem = 0.50 * km
elif km > 200:
    passagem = 0.45 * km

print("Você pagará %2.2sR$" %(passagem))
