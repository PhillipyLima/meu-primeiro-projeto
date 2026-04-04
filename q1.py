# Elabore um algoritmo que receba dois números, calcule a multiplicação entre eles e apresente o
# resultado.
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
resultado = num1 * num2
print("O resultado da multiplicação é: ", resultado)

#Desenvolva um algoritmo que receba cinco números, calcule a média aritmética e apresente o
#resultado final.
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
num4 = float(input("Digite o quarto número: "))
num5 = float(input("Digite o quinto número: "))
resultado = (num1 + num2 + num3 + num4 + num5)/5
print("O resultao da média é: ", resultado)

# Construa um algoritmo que receba o valor de um produto e calcule o preço final considerando um
# acréscimo de 8% de imposto.

valororiginal = float(input("Digite o valor sem imposto: "))
valorcomimposto = valororiginal*1.08
print(valorcomimposto)

# Elabore um algoritmo que receba dois números e apresente o resultado da subtração entre eles.
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
subtracao = num2-num1
print("O resultado da subtração é ", subtracao)


#Construa um algoritmo que receba a altura e o peso de uma pessoa e calcule o Índice de Massa
#Corporal (IMC).
# peso/altura*altura
altura = float(input("Digite a altura de uma pessoa: "))
peso = float(input("Digite o peso da pessoa: "))
imc = peso/(altura*altura)
print('o resultado do imc é',  imc)


# Elabore um algoritmo que receba a temperatura em graus Celsius e apresente o valor convertido
# para graus Fahrenheit.
# (c° x 1.8) + 32
celsius = float(input('digite a temperatura'))
farenheit =  (celsius*1.8) + 32
print( 'o valor é ', farenheit )

# Construa um algoritmo que receba a quantidade de horas trabalhadas por um funcionário e o valor
# da hora trabalhada, calculando o salário total.
horas_trabalhadas=int(input("digite a hora trabalhada:"  ))
valor_da_hora_trabalhada=int(input("digite o valor da hora trabalhada:"))
salario  =  horas_trabalhadas*valor_da_hora_trabalhada
print("o salario è",  salario)
