##Leia um número e:
##Se for par e positivo → “Par positivo”; 
##Se for par e negativo → “Par
#negativo”; Caso contrário → “Ímpar”.

x = int(input("digite um numero"))
if x % 2 == 0 and x > 0:
    print("Par positivo")
elif x % 2 == 0 and x < 0:
    print("Par negativo")
else:
    print("Ímpar")