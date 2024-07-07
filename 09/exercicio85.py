'''Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e 
cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
No final, mostre os valores pares e ímpares em ordem crescente.'''
numero = [[],[]]
for c in range(1, 8):
    n = int(input("digite um numero: "))
    if n % 2 == 0:
        numero[0].append(n)
    else:
        numero[1].append(n)
numero[0].sort()
numero[1].sort()
print(f"Pares:{numero[0]}")
print(f"Impares:{numero[1]}")
