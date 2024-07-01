import random
aleatorio = random.randint(1, 10)
print("pense em um numero de 0 a 10")   
acertou = False  
palpite = 0
while not acertou:
    num = int(input("digite o numero: "))
    palpite += 1
    if num == aleatorio:
        print("acertou.")
        acertou = True
    else:
        if num > aleatorio:
            print("menos...")
        elif num < aleatorio:
            print("mais...")
print(f"acertou com {palpite} tentativa(s).")