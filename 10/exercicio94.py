'''Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando 
os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média'''
pessoas = {}
lista = []
soma = 0
media = 0

while True:
    pessoas.clear()
    pessoas['nome'] = str(input("Qual o nome da pessoa? "))
    while True:
        pessoas['sexo'] = str(input("Qual o sexo da pessoa? [M/F] ")).upper()
        if pessoas['sexo'] in "MF":
            break
        print("ERRO! POR FAVOR, APENAS M OU F.")
    pessoas['idade'] = int(input("Qual a idade da pessoa? "))
    soma += pessoas['idade']
    lista.append(pessoas.copy())
    while True:
        continuar = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
        if continuar in 'SN':
            break
        print("RESPOSTA ERRADA. POR FAVOR, APENAS S OU N.")
    if continuar == 'N':
        break

media = soma / len(lista)
print()
print(f"Ao todo temos {len(lista)} pessoas cadastradas.")
print(f"A média de idade é de: {media:5.2f} anos.")
print("As mulheres cadastradas foram:")
for p in lista:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' ')
print()
print("Pessoas com idade acima da média:")
for p in lista:
    if p['idade'] >= media:
        print("    ")
        for a, b in p.items():
            print(f'{a} = {b}', end='; ')
        print()
