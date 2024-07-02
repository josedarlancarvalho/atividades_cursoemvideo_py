import random 
comp = random.randint(1, 10)
a = 0

while a < 3:
    a += 1
    num = int(input("digite um numero: "))
    op = str(input("Par ou Impar? [P/I]: ")).upper().strip()[0]
    soma = comp + num
    if soma % 2 == 0 and op in "P":
        print(f"voce ganhou.{comp} foi o numero escolhido pelo computador.")
    elif soma % 2 == 0 and op in "I":
        print(f"voce perdeu.{comp} foi o numero escolhido pelo computador.")
    elif soma % 2 != 0 and op in "I":
        print(f"voce ganhou.{comp} foi o numero escolhido pelo computador.")
    elif soma % 2 != 0 and op in "I":
        print(f"voce perdeu.{comp} foi o numero escolhido pelo computador.")
print("fim")