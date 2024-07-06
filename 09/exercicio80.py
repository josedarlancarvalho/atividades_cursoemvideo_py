'''Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em
uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela'''

lista = []
for c in range (0,5):   
    l = int(input("digite um numero: "))
    if c == 0 or l > lista[-1]:
        lista.append(l)
    else:
        p = 0
        while p < len(lista):
            if l <= lista[p]:
                lista.insert(p, l)
                break
        p +=1
print(f"lista ordenada: {lista}")