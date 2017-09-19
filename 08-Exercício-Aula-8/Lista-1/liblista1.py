
def testVogal(testavogal):
    if testavogal == 'a' or testavogal == 'e' or testavogal == 'i' or testavogal == 'o' or testavogal == 'u':
        return True
    else:
        return False

def calculaMaior(numero1, numero2):
    if numero1 > numero2:
        return numero1
    else:
        return numero2
    
def testaMultiplo4(num):
    if num % 4 == 0:
        return True
    else:
        return False

def testaDivisor(num1, num2):
    if num1 % num2 == 0:
        return True
    else:
        return False
