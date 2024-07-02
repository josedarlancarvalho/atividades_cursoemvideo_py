n_1 = int(input("qual o primeiro termo? "))
n_2 = int(input("qual a razao? "))
termo = n_1
n = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while n <= total:
        print(f"{termo} -> ", end ='')
        termo += n_2
        n += 1
    mais = int(input("quantos termos voce quer mostrar a mais?"))
print("fim")
