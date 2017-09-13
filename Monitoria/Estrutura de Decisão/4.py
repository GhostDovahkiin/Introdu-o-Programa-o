# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra = str.lower(input("Digite uma letra: "))
if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print("{} é uma vogal" .format(letra))
else:
    print("{} é uma consoante" .format(letra))
