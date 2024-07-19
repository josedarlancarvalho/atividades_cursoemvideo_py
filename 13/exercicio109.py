'''Exercício Python 109: Modifique as funções que form criadas no desafio 107 
para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai 
ser ou não formatado pela função moeda(), desenvolvida no desafio 108.'''
from functions import numeros

numero = int(input("Digite um número: "))

print(f"O dobro de {numeros.moedas(numero)} é {numeros.moedas(numeros.dobro(numero), True)}")
print(f"A metade de {numeros.moedas(numero)} é {numeros.moedas(numeros.metade(numero), True)}")
print(f"O {numeros.moedas(numero)} com aumento de 10% é {numeros.moedas(numeros.aumentar(numero), True)}")
print(f"O {numeros.moedas(numero)} com desconto de 10% é {numeros.moedas(numeros.diminuir(numero), True)}")