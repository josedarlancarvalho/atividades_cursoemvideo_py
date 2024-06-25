import random 
n = int(input("Escolha um numero de 1 a 5:"))
c = random.randint(1, 5)
if n == c:
    print("voce acertou o numero, parabens.")
else:
    print(f"voce errou o numero. o numero escolhido pela maquina era {c}")
