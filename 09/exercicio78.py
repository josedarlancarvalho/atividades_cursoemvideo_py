lista = []
maior = menor = 0
for c in range(0, 5):
    lista.append(int(input("digite um valor: ")))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print('='*30)
for a, b in enumerate(lista):
    print(f'{a} posicao tem o valor {b}')

print(f'maior valor digitado: {maior}')
print(f'menor valor digitado: {menor}')

