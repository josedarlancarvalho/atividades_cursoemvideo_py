'''Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma 
semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt(‘Digite um n: ‘)'''
def leiaInt(n):
    while True:
        num = input(n) 
        if num.isnumeric(): 
            return int(num) 
        else:
            print("ERRO. DIGITE UM NÚMERO:") 

n = leiaInt("Digite um número: ")
print(f"{n} foi o número que você digitou.")
