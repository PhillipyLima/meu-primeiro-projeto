##18. Leia um número e: Mostre se ele é par positivo, par negativo, impar positivo, impar negativo ou
##neutro.

numero= int(input("digite um numero:"))
if numero==0:
    print("neutro")
elif numero % 2==0:  ##par
    if numero >0:
             print("par positivo")  
    else:
        print("par negativo")
    else:   ######impar
if numero>0:
    print("impar positivo")
else:
    print("impar negativo")