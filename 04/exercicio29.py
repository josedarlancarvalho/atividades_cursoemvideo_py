velocidade = float(input("qual a velocidade do carro? "))
multa = (velocidade - 80) * 7
if velocidade <= 80:
    print("tenha um otimo dia.")
else:
    print("voce foi multado.")
    print(f"a multa é R${multa}")