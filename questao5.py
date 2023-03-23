#5 - Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

print("\n** Questão 5 - PESO IDEAL - HOMEM & MULHER **\n")

sexo = input("Selecione seu sexo: (M - Masculino), (F - Feminino): ")
altura = float(input("Digite sua altura: "))

if sexo == 'm':
    peso_ideal = (72.7 * altura) - 58
    print(f"Você é homem e tem uma altura de {altura}, seu peso ideal é: {peso_ideal: .2f} KG")
if sexo == 'f':
    peso_ideal = (62.1 * altura) - 44.7
    print(f"Você é mulher e tem uma altura de {altura}, seu peso ideal é: {peso_ideal: .2f} KG")
