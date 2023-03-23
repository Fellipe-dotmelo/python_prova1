#7 - Faça um Programa que peça dois números e imprima o maior deles.

print("\n** Questão 7 - MAIOR NÚMERO **\n")

num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))

if num1 > num2:
    print(f"O maior número é: {num1}, que é o primeiro")
if num2 > num1:
    print(f"O maior número é: {num2}, que é o segundo")
else:
    print(f"Os números inseridos foram iguais, número 1: {num1} e número 2: {num2}")
