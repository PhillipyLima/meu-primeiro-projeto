# 12. Leia dois números e: Mostre a soma; Mostre qual é maior ou se são iguais.

numero1= int(input("digite um numero:"))
numero2= int(input("digite outro numero:"))
soma= int(numero1+numero2)
print("a soma é:", (soma))
 if numero1 > numero2:
   print("maior é:", (numero1))
     elif numero2 > numero1:
      print("maior é:", (numero2))
        else:
          print("os numeros são iguais")