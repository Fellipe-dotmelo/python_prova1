#2 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês.

print("\n** SISTEMA CÁLCULO DE HORAS **\n")

hora = float(input("Digite o quanto você ganha por hora: "))
quantidade_hora = int(input("Digite quantas horas você trabalhou este mês: "))

total_salario = hora*quantidade_hora

print(f"O total do salário deste trabalhador é: {total_salario}")