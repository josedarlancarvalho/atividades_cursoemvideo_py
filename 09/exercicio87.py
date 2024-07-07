'''Exercício Python 087: Aprimore o desafio anterior, mostrando no final:                                                    
A) A soma de todos os valores pares digitados.v                                                                
B) A soma dos valores da terceira coluna.                                                                                                                
C) O maior valor da segunda linha.'''
matriz = [0, 0, 0],[0, 0, 0],[0, 0, 0]
pares = terceira_c = segunda_l =  0
for c in range(0,3):
    for l in range(0,3):
        matriz[c][l] = int(input("digite um valor: "))
        if matriz[c][l] % 2 == 0:
            pares += matriz[c][l]
        if matriz[c][l] == matriz[c][2]:
            terceira_c += matriz[c][2]
for c in range(0,3):
    for l in range(0,3):
        print(f"[{matriz[c][l]:^5}]", end = '')
    print()
print(f"soma dos pares da matriz: {pares}")
print(f"soma dos valores da terceira coluna: {terceira_c}")
for l in range(0, 3):
    if l == 0:
        segunda_l = matriz[1][l]
    elif matriz[1][l] > segunda_l:
        segunda_l = matriz[1][l] 
print(f"maior valor da segunda linha é: {segunda_l}")