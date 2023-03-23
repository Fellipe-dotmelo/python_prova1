'''12 - Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.'''

print("\n** Questão 12 - Masculino/Feminino **")

sexo_selecao = input("Insira seu sexo: [M - Masculino], [F - Feminino]: ")

if sexo_selecao == 'F' or sexo_selecao == 'f':
    print("Sexo Feminino")
elif sexo_selecao == 'M' or sexo_selecao == 'm':
    print("Sexo Masculino")
else:
    print("Sexo Inválido.")