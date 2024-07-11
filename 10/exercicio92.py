'''Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e 
cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário 
receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, 
com quantos anos a pessoa vai se aposentar.'''

pessoa = {}
pessoa ['nome'] = str(input("qual o nome?"))
nascimento = int(input("qual ano que voce nasceu?"))
pessoa ['carteira'] = input("voce tem carteira de trabalho? Digite 0 para nao.")
pessoa ['idade'] = 2024 - nascimento

if '0' in pessoa['carteira'] :
    print(f"nome: {pessoa['nome']}")
    print(f"{pessoa['nome']} tem {pessoa['idade']} anos.")
    print("nao tem carteira de trabalho.")
else:
    pessoa ['contratacao'] = int(input("qual seu ano de contratacao? "))
    pessoa ['salario'] = int(input("qual seu salario? "))
    pessoa ['aposentar'] = pessoa['contratacao'] + 36
    print(f"nome: {pessoa['nome']}")
    print(f"{pessoa['nome']} tem {pessoa['idade']} anos.")
    print(f"carteira de trabalho: {pessoa['carteira']}")
    print(f"{pessoa['nome']} recebe R${pessoa['salario']} por mes.")
    print(f"{pessoa['nome']} vai se aposentar com {pessoa['aposentar'] - nascimento} anos.")