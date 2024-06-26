import random
print("""
      Opcoes:

      [0] Pedra
      [1] Papel
      [2] Tesoura

    """)
jogada = int(input("Qual sua jogada?"))
computador = random.randint(0, 2)

if jogada == computador:
    print("Empate")
elif jogada == 0 and computador == 1 :
    print("Computador ganhou")
elif jogada == 0 and computador == 2 :
    print("Jogador ganhou")
elif jogada == 1 and computador == 2 :
    print("computador ganhou")
elif jogada == 1 and computador == 0 :
    print("Jogador ganhou")
elif jogada == 2 and computador == 0 :
    print("computador ganhou")
elif jogada == 2 and computador == 1 :
    print("Jogador ganhou")
else:
    print("opcao invalida")