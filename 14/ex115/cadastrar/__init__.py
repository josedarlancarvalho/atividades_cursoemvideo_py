cadastradas = []

def cadastrar():
    pessoa = {}
    pessoa['nome'] = str(input('Digite seu nome: '))
    pessoa['idade'] = int(input('Digite sua idade: '))
    cadastradas.append(pessoa)
    print('-' * 30)
    print('Pessoa cadastrada.')
    print('-' * 30)