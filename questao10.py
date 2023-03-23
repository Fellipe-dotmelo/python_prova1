''''10 - Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo
até que o usuário informe um valor válido.'''

print("\n** Questão 10 - Zero/Dez **\n")

contador = 1
while (contador <= 100):
    nota = int(input("Insira uma nota entre zero e dez: "))
    if nota < 0 and nota > 10:
        print("Você inseriu um valor inválido.")
    if nota >= 0 and nota <= 10:
        print("Você inseriu um valor válido.")
        break
    contador   = contador + 1