# CÓDIGO CERTO 
altura = float(input("Insira sua altura: "))
if altura <= 1.40:
    estatura = "Estatura Baixa"
elif altura < 1.65:
    estatura = "Estatura Mediana"
else:
    estatura = "Estatura Alta"
print(estatura)


# CÓDIGO ERRADO
altura = float (input())
if (altura <= 1.40):
 print("Estatura Baixa") # Redundância de print
else: #Uso indevido de Else
 if (altura < 1.65): # Não precisava de fazer outro teste, um elif resolveria o problema.
 print("Estatura Mediana") # Redundância de print
 else:
 print("Estatura Alta") # Redundância de print
