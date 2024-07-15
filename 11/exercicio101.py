'''Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber 
como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma 
pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''
def voto(ano):
    idade = 2024 - ano
    if idade < 16:
        print(f"com {idade} anos o voto é negado")
    if idade > 16 and idade < 18:
        print(f"com {idade} anos o voto é opcional")
    if idade > 18:
        print(f"com {idade} anos o voto é obrigatorio")
idade = int(input("qual o ano que voce nasceu?"))
voto(idade)