#####11. Leia um número e:
#  Se for par e positivo → “Par positivo”; 
# Se for par e negativo → “Par
#negativo”; 
# Caso contrário → “Ímpar”.

numero= int(input("digite um numero:"))

if numero % 2 == 0 and numero > 0:
    print("par positivo")
elif numero % 2 == 0 and numero < 0:
    print("par negativo")
else:
    print("impar")



