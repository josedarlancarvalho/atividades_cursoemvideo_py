from datetime import date
atual = date.today().year
data_nascimento = int(input("qual o ano do nascimento?"))

idade = atual - data_nascimento

if idade == 18:
    print(f"Voce tem que se alistar esse ano.")
elif idade < 18:
    saldo = 18 - idade
    print(f"ainda falta {saldo} para se alistar.")
    ano = atual + saldo
    print(f"seu alistamento sera me {ano}")
elif idade > 18:
    saldo = idade - 18
    print(f"voce deveria ter se alistado a {saldo} anos")
    ano = atual - saldo
    print(f"seu alistamento foi em {ano}")