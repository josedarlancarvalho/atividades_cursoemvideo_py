'''Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade 
de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o 
total de gols feitos durante o campeonato.'''
jogador = {}
gols = []
jogador['nome'] = str(input("qual o nome do jogador?"))
partidas = int(input("quantas partidas ele jogou?"))

for c in range(0, partidas):
        gols.append(int(input(f"quantos gols ele fez na partida {c+1}?")))
jogador ['gols'] = gols
jogador ['gols_totais'] = sum(gols)
print()
print(jogador)
print()
for y, a in jogador.items():
    print(f"o campo {y} tem o valor {a}  ")
print()
print(f"o {jogador['nome']} tem {partidas} partidas jogadas.")
for a, b in enumerate(jogador['gols']):
      print(f"na partida {a} ele fez {b} gols.")
print()
print(f"foi um total de {jogador['gols_totais']} gols.")