'''Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, 
sabendo que o vencedor tirou o maior número no dado.'''
from random import randint 
from operator import itemgetter
jogadores = {}
ranking = []
for c in range (1,5):
    jogadores [f'jogador{c}'] = randint(1,6)

for k, v in jogadores.items():
    print(f"{k} tirou {v}")

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

for c, i in enumerate(ranking):
    print(f"{c+1} posicao foi o {i[0]} com {i}")