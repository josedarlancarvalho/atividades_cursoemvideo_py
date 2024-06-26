peso = float(input("digite seu peso"))
altura = float(input("digite sua altura"))

imc = peso / (altura * altura)
print(f"Seu IMC é:{imc:.2f}")
if imc <= 18.5:
    print("voce esta abaixo do peso.")
elif imc > 18.5 and imc < 25:
    print("voce esta no peso ideal.")
elif imc > 25 and imc < 30:
    print("voce esta com sobrepeso.")
elif imc > 30 and imc < 40:
    print("voce esta obeso.")
else:
    print("voce esta com obesidade morbida.")