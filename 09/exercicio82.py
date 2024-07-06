'''Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
 Depois disso, crie duas listas extras que vão conter apenas os valores 
pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''
lista = []
par = []
impar = []
while True:
    a = int(input("digite um numero:"))
    lista.append(a)
    if a % 2 == 0:
        par.append(a)
    else:
        impar.append(a)
    continuar = str(input("quer continuar? [s/n]")).strip()[0].upper()
    if 'N' in continuar:
        break
print(f"Lista: {lista}")
print(f"Numeros pares da lista: {par}")
print(f"Numeros impares da lista: {impar}")

