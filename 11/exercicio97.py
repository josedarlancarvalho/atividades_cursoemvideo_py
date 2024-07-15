'''Exercício Python 097: Faça um programa que tenha uma função chamada escreva(),
que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.      '''
def linha(frase):
    print('-' * (len(frase)))
    print(f'{  frase}')
    print('-' * (len(frase)))

a = str(input("digite a frase:"))
linha(a)