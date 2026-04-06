#20. Leia um valor e: verifique se eles está entre 0 e 100, caso o número esteja fora do intervalo,
##mostre na tela o valor.

valor= float(input("digite um numero:"))
if valor<0 or valor>100:
    print("valor fora do intervalo:", (valor))
else:
    print("dentro do intervalo")