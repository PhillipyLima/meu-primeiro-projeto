####13. Leia um número e: Se for maior que 100 → mostre metade; Senão → mostre o dobro.

x= float(input("digite um numero:"))
if x>100:
    metade = int(x)/2
    print("metade:", (metade))
else:
    dobro = int(x)*2
    print("dobro é:", (dobro))