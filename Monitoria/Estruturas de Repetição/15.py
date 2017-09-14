fib = int(input("Numº: "))
ult = 0
pen = 1
for i in range(fib):
    pen += ult
    ult = pen - ult
    print(ult)
