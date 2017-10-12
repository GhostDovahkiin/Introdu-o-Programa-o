numero = list(str(input("Número: ")))
res = str(numero)
if res.find("-") > 0:
        numero.remove("-")
        if len(numero) == 7:
                numero.insert(0, "3")
                numero.insert(4, "-")
                print("Há 7 dígitos. Irei inserir um dígito 3 no início.")
        elif len(numero) == 8:
                numero.insert(4, "-")
        else:
                print("Número inválido")
                exit()
        semformat = numero
else:
        if len(numero) == 7:
                numero.insert(0, "3")
                numero.insert(4, "-")
                print("Há 7 dígitos. Irei inserir um dígito 3 no início.")
        elif len(numero) == 8:
                numero.insert(4, "-")
        else:
                print("Número inválido")
                exit()
        semformat = numero
comformat = numero
str(comformat).strip('[]')
print("Número com formatação: {}" .format(''.join(map(str, comformat))))
semformat.remove("-")
str(semformat).strip('[]')
print("Número sem formatação: {}" .format(''.join(map(str, semformat))))
