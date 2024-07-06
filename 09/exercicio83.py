'''Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu 
aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''
exp = str(input("digite a expressao: "))
pilha = []
for c in exp:
    if c == '(':
        pilha.append('(')
    elif c == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print("sua expressao é valida")
else:
    print("sua expressao nao é valida.")