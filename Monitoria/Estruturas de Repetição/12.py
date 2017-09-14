#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada
tab = int(input("Tabuada de: ")) 
for i in range(1,11):
    res = tab * i
    print("{} x {} = {}" .format(tab,i, res))
    
