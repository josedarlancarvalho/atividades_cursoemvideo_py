'''Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos 
preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''
lista = ('caderno', 20,
         'lapis', 5,
         'regua', 3,
         'borracha', 2,
         'caneta', 1.5,
         'estojo', 7)
for n in range (0, len(lista)):
    if n % 2 == 0:
        print(f"{lista[n]:.<15}", end = '')
    else:
        print(f"R${lista[n]:>7.2f}")