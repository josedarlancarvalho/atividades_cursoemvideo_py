'''Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(),
dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.'''
from functions import numeros

numero = int(input("digite um numero: "))
print(f"o dobro de {numero} é {numeros.dobro(numero)}")
print(f"a metade de {numero} é {numeros.metade(numero)}")
print(f"o {numero} com aumento de 10% é {numeros.aumentar(numero)}")
print(f"o {numero} com desconto de 10% é {numeros.diminuir(numero)}")