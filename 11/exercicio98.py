'''Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. 
Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1                                                                                                                                              
b) de 10 até 0, de 2 em 2                                                                                                                                            
c) uma contagem personalizada'''
def contador(inicio, fim, passo):
    print('-'*30)

    if passo == 0:
        passo = 1
    if inicio < fim and passo < 0:
        passo = abs(passo)
    elif inicio > fim and passo > 0:
        passo = -passo
    
    print(f"Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}:")
    for c in range(inicio, fim + (1 if passo > 0 else -1), passo):
        print(c, end=' ')
    print('FIM')
    
    print('-'*30)
print('-'*30)
print("Contagem de 1 até 10 de 1 em 1:")
for c in range(1, 11, 1):
    print(c, end=' ')
print('FIM')
print('-'*30)

print("Contagem de 10 até 0 de 2 em 2:")
for c in range(10, -1, -2):
    print(c, end=' ')
print('FIM')
print('-'*30)

print("Agora é sua vez de personalizar a contagem.")
i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
contador(i, f, p)
