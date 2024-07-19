'''Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional
 chamada moeda() que consiga mostrar os números como um valor monetário formatado.'''
from functions import numeros

numero = int(input("Digite um número: "))

print(f"O dobro de {numeros.moedas(numero)} é {numeros.moedas(numeros.dobro(numero))}")
print(f"A metade de {numeros.moedas(numero)} é {numeros.moedas(numeros.metade(numero))}")
print(f"O {numeros.moedas(numero)} com aumento de 10% é {numeros.moedas(numeros.aumentar(numero))}")
print(f"O {numeros.moedas(numero)} com desconto de 10% é {numeros.moedas(numeros.diminuir(numero))}")