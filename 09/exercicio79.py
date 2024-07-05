'''Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos 
e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. 
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''
lista = list()
a = 0
while True:
    l = int(input('digite o valor: '))
    if l not in lista:
        lista.append(l)
    else:
        print("valor repetido nao pode.")
    continuar = str(input("quer continuar? [S/N]")).strip()[0].upper()
    if 'N' in continuar:
        break
lista.sort()
print(lista)
    