print("\n** Questão 9 - DIA SEMANA **")
semana = ["Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado"]

dia_semana = int(input("Selecione o dia da semana de 1 à 7: "))

match dia_semana:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda-feira")
    case 3:
        print("Terça-feira")
    case 4:
        print("Quarta-feira")
    case 5:
        print("Quinta-feira")
    case 6:
        print("Sexta-feira")
    case 6:
        print("Sábado")
    case _:
        print("Dia inválido")