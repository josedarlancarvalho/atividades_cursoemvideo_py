'''Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois 
parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor
 lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.'''
def fatorial(n, show=False):
    a = n 
    cont = n 
    
    if show:
        print(f"{n}", end="") 
    while cont > 1:  
        cont -= 1 
        a *= cont
        if show:
            print(f" x {cont}", end="") 
    if show:
        print(f" = {a}")  
    return a 
print(fatorial(5)) 
print(fatorial(5, show=True))
