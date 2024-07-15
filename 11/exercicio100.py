'''Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas 
sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a 
segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.'''
from random import randint
numeros= []
soma_par = 0
def sorteia():
    for c in range(0,5):
        sorteados = randint(1,10)
        numeros.append(sorteados)
sorteia()
print(numeros)
def somaPar():
    soma = 0
    for valor in numeros:
        if valor % 2 == 0:
            soma += valor 
    print(soma)
somaPar()

