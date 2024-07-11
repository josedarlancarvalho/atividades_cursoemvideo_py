'''Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, 
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''
jogador = {}
time = []
gols = []

while True:
    jogador.clear()
    jogador['nome'] = str(input("Qual o nome do jogador? "))
    partidas = int(input("Quantas partidas ele jogou? "))
    gols.clear()
    for c in range(partidas):
        gols.append(int(input(f"Quantos gols ele fez na partida {c + 1}? ")))
    jogador['gols'] = gols[:]
    jogador['gols_totais'] = sum(gols)
    time.append(jogador.copy())
    while True:
        continuar = str(input("Quer continuar? [S/N] ")).upper().strip()
        if continuar in 'SN':
            break
        print("Responda apenas S ou N.")
    if continuar == 'N':
        break

print()
print('cod ', end='')
for i in jogador.keys():
    print(f"{i:<15}", end='')
print()
for k, c in enumerate(time):
    print(f"{k:>3} ", end='')
    for d in c.values():
        print(f"{str(d):<15}", end='')
    print() 

print()
while True:
    busca = int(input("Quer os dados de qual jogador? (999 para parar) "))
    if busca == 999:
        break
    if busca >= len(time):
        print(f"Não existe jogador com esse código {busca}.")
    else:
        print(f"Levantamento do jogador {time[busca]['nome']}: ")
        for i, g in enumerate(time[busca]['gols']):
            print(f"    No jogo {i + 1} fez {g} gols.")
    print()
