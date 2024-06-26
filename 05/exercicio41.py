from datetime import date
data_nascimento = int(input("em que ano o atleta nasceu?"))
atual = date.today().year
idade = atual - data_nascimento
if idade < 7:
    print("Mirim")
elif idade > 7 and idade < 14:
    print("infantil")
elif idade > 14 and idade < 19:
    print("Junior")
elif idade >19 and idade < 25:
    print("senior")
elif idade > 25:
    print("master")
