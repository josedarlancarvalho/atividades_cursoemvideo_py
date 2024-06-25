viagem = int(input("digite a distancia da viagem:"))
perto = viagem * 0.5
longe = viagem * 0.45
if viagem <= 200:
    print(f"o valor da viagem é {perto}")
else:
    print(f"o valor da viagem é {longe}")