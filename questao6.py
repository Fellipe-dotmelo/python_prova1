'''6 - João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
(50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia
a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite
e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.'''

print("\n** Questão 6 - EXCESSO DE PESCA **\n")

valor_kg = 4
kg_regulamentar = 50
peso_peixes = int(input("Quantos KG's foram pescados, hoje: "))

multa = (peso_peixes - 50) * 4

if peso_peixes == 50:
    print("O peso está dentro do regulamento, não haverá multa.")
if peso_peixes > kg_regulamentar:
    print(f"Você extrapolou a quantidade máxima em: {peso_peixes}, terá de pagar: R$ {multa}")