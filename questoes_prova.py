print('Ao acontecer um crime no clube RosaLinda, os investigadores decidem interrogar as pessoas que lá estavam,\nvocê como pessoa presente '
      'deve responder as perguntas listadas abaixo com [sim] ou [não]\n\n')

pergunta_1 = input('Telefonou para a vítima? ')

contagem = 0

if pergunta_1 == 'sim':
    contagem1 = contagem +1
else:contagem1 = contagem + 0

pergunta_2 = input('Esteve no local do crime? ')

if pergunta_2 == 'sim':
    contagem2 = contagem1 + 1
else:
    contagem2 = contagem1 + 0

pergunta_3 = input('Mora perto da vítima? ')

if pergunta_3 == 'sim':
    contagem3 = contagem2 + 1
else:
    contagem3 = contagem2 + 0

pergunta_4 = input('Devia para a vítima? ')

if pergunta_4 == 'sim':
    contagem4 = contagem3 + 1
else:
    contagem4 = contagem3 + 0

pergunta_5 = input('Já trabalhou com a vítima? ')

if pergunta_5 == 'sim':
    contagem = contagem4 + 1
else:
    contagem = contagem4 + 0

if contagem == 2:
    print('Suspeita')
if contagem == 3 or contagem == 4:
    print('Cúmplice')
if contagem == 5:
    print('Assassino')
if pergunta_1 == 'nao' and pergunta_2 == 'nao' and pergunta_3 == 'nao' and pergunta_4 == 'nao' and pergunta_5 == 'nao':
    print('Inocente')