#9 - Faça um Programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

print("\n** Questão 9 - DIA SEMANA **")
print("Dias semana: \n 1- Domingo, \n 2- Segunda-feira, \n 3- Terça-feira, \n 4- Quarta-feira, \n 5- Quinta-feira, \n 6- Sexta-feira, \n 7- Sábado\n ")

dia_semana = int(input("Selecione o dia da semana: "))

if dia_semana == 1:
    print("O dia correspondente é DOMINGO")
if dia_semana == 2:
    print("O dia correspondente é SEGUNDA-FEIRA")
if dia_semana == 3:
    print("O dia correspondente é TERÇA-FEIRA")
if dia_semana == 4:
    print("O dia correspondente é QUARTA-FEIRA")
if dia_semana == 5:
    print("O dia correspondente é QUINTA-FEIRA")
if dia_semana == 6:
    print("O dia correspondente é SEXTA-FEIRA")
if dia_semana == 7:
    print("O dia correspondente é SÁBADO")
else:
    print("Valor Inválido, consulte os dias acima")