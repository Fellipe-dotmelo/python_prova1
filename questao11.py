'''11 - Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
Depois modifique o programa para que ele mostre os números um ao lado do outro.'''

print("\n** Questão 11 - 1 à 20 **")

for numeros in range(21):
    print(numeros)

for cont in range(21):
    if cont < 20:
        print(cont, end=", ")
    else:
        print(cont)