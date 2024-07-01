n_1 = int(input("qual o primeiro termo? "))
n_2 = int(input("qual a razao? "))
termo = n_1
n = 1
while n <= 10:
    print(f"{termo} -> ", end ='')
    termo += n_2
    n += 1