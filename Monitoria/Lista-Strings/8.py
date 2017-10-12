print("PALÍNDROMO")
str1 = list(str.lower(input("Digite uma palavra, ou frase: ")))
str1.remove(" ") 
str2 = str1[::-1]   
if str1 == str2:
    print("É UM PALÍNDROMO")
else:
    print("NÃO É UM PALÍNDROMO")
