'''Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''
gasto_tot = mais_1000 = 0
mais_barato = None
nome_mais_barato = ''
while True:
    nome_prod = str(input("Qual o nome do produto? "))
    preco_prod = float(input("Qual o valor do produto? "))
    gasto_tot += preco_prod
    if preco_prod > 1000:
        mais_1000 += 1
    if mais_barato is None or preco_prod < mais_barato:
        mais_barato = preco_prod
        nome_mais_barato = nome_prod
    continuar = str(input("Quer continuar? [S/N]")).upper().strip()[0]
    if continuar in 'N':
        break
    
print(f"R${gasto_tot} foi o valor total da compra.")
print(f"Teve {mais_1000} produtos que custaram mais de R$1000.")
print(f"o item mais barato foi {nome_mais_barato} de valor: {mais_barato}")