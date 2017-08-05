anos = int(input("Digite seus anos de idade: "))
meses = int(input("Digite seus meses de idade: "))
dias = int(input("Digite seus dias de idade: "))
dias1 = anos*365
dias2 = meses*30
dias3 = dias1 + dias2 + dias
print("Sua idade total em dias é: %s" %dias3)
