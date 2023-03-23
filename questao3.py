'''
3 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo.
a soma do triplo do primeiro com o terceiro. O terceiro elevado ao cubo.
'''

print("\nQuestão 3 - NÚMEROS\n")

num1 = int(input("Insira o primeiro número inteiro: "))
num2 = int(input("Insira o segundo número inteiro: "))
num3 = float(input("Insira o terceiro número real: "))

resultado1 = (num1*2) + (num2/2)
resultado2 = (3*num1) + num3
resultado3 = num3**3

print(f"O produto do dobro do primeiro com a metade do segundo: {resultado1}")
print(f"A soma do triplo do primeiro com o terceiro: {resultado2}")
print(f"O terceiro elevado ao cubo: {resultado3}")
