'''Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as 
dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
'''

def area(larg,comp):
    a = larg * comp
    print(f"a area é {a}m²")


a= int(input('largura:'))
b= int(input('comprimento:'))
area(a, b)
