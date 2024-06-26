nota_1 = float(input("Digite a primeira nota"))
nota_2 = float(input("Digite a segunda nota"))
media = (nota_1 + nota_2) / 2

if media >= 7:
    print("parabens. voce foi aprovado por media.")
elif media < 7 and media > 5:
    print("voce ficou na final. estude")
else:
    print("voce foi reprovado direto.")