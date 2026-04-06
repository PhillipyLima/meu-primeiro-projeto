#14. Leia um valor e: Converta para inteiro; Se for múltiplo de 3 → “Múltiplo de 3”; Senão → “Não é


valor= int(input("digite um numero inteiro:"))
if valor % 3 == 0:
    print("multiplo de 3")
else:
    print("não é multipo")