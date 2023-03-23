'''8 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato.'''

print("\n** Questão 8 - PRODUTO MAIS BARATO **\n")

p1 = int(input("Insira o primeiro produto: "))
p2 = int(input("Insira o segundo produto: "))
p3 = int(input("Insira o terceiro produto: "))

if p1 < p2 and p1 < p3:
    print(f"O primeiro produto é o mais barato, pois o valor é: {p1}")

if p2 < p1 and p2 < p3:
    print(f"O segundo produto é o mais barato, pois o valor é: {p2}")

if p3 < p1 and p3 < p2:
   print(f"O terceiro produto é o mais barato, pois o valor é: {p3}")