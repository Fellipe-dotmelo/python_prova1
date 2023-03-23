'''13 - Faça um Programa que leia três números e mostre o maior e o menor deles.'''

print("\n** Questão 13 - Maior e Menor **")

num1 = int(input("Insira o número 1: "))
num2 = int(input("Insira o número 2: "))
num3 = int(input("Insira o número 3: "))

print("\n O maior número \n")

if num1 > num2 and num1 > num3:
    print(f"O maior número é: {num1}, que é o primeiro")

if num2 > num1 and num2 > num3:
    print(f"O maior número é: {num2}, que é o segundo")

if num3 > num1 and num3 > num2:
    print(f"O maior número é: {num3}, que é o segundo")


print("\n O menor número \n")

if num1 < num2 and num1 < num3:
    print(f"O menor número é: {num1}, que é o primeiro")

if num2 < num1 and num2 < num3:
    print(f"O menor número é: {num2}, que é o segundo")

if num3 < num1 and num3 < num2:
    print(f"O menor número é: {num3}, que é o segundo")