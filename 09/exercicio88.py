'''Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.'''
from random import randint
teste = []
jogo = int(input("Quantos jogos você quer? "))
for l in range(jogo):
    jogo_atual = []
    while len(jogo_atual) < 6:
        computador = randint(1, 60)
        if computador not in jogo_atual:
            jogo_atual.append(computador)
    jogo_atual.sort() 
    teste.append(jogo_atual)  
for c, jogo in enumerate(teste, 1):
    print(f"jogo numero {c}: {jogo}")
print("Fim")
