print("PALÍNDROMO")
str1 = list(str.lower(input("Digite uma palavra, ou frase: ")))
for i in str1:
        if i == " ":
            str1.remove(" ")
            print(str1)
        else:
            break
if str1 == str1[::-1] :
    print("É UM PALÍNDROMO")
else:
    print("NÃO É UM PALÍNDROMO")
