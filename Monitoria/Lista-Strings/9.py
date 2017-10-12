unit = ["um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove","dez", "onze", "doze", "treze", ''"catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
dezen = ["vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
n = int(input("Digite um número: "))
if n <= 9:
  print(unit[n-1])
elif n > 9 and n <= 19:
    print(unit[n-1])
else:
    dez = (n//10)
    uni = n%10
    print("{} e {}".format(str.upper(dezen[dez-2]),str.upper(unit[uni-1])))
