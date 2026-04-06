###16. Leia um valor e: Mostre o tipo; Se for numérico (após conversão) → mostre o quadrado.

valor= input("digite um valor:")
print("tipo original é:",{type(entrada)})

#converter para numero

numero= float(valor)
quadrado= int(numero)**2
print("quadrado:", (quadrado))
