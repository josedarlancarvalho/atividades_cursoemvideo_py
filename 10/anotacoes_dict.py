dados = dict() 
dados = {} #ambas servem´para criar um dicionario

dados ={'nome':'pedro', 'idade':'25'} #adicionando dados no dicionario
print(dados['nome'])# retorna apenas 'pedro'

dados['sexo']= 'M'#adicionando dados novos. append nao funciona no dict
print(dados)

del dados['idade']#antes desse comando:{'nome': 'pedro', 'idade': '25', 'sexo': 'M'}
print(dados)      #depois {'nome': 'pedro', 'sexo': 'M'}

filme ={
    'filme': 'star wars',
    'ano':'1977',
    'diretor': 'george lucas'
}

print(filme)#{'filme': 'star wars', 'ano': '1977', 'diretor': 'george lucas'}

print(filme.values())# OS VALORES SAO : dict_values(['star wars', '1977', 'george lucas'])
print(filme.keys()) # as chaves sao: dict_keys(['filme', 'ano', 'diretor'])
print(filme.items()) #os itens sao todos os itens do dict: dict_items([('filme', 'star wars'), ('ano', '1977'), ('diretor', 'george lucas')])

for k, v in filme.items():  #o filme é star wars
    print(f"o {k} é {v}")   #o ano é 1977
                            #o diretor é george lucas

filme_1 ={
    'filme': 'avengers',
    'ano':'2012',
    'diretor': 'joss whedon'
}

filme_2 ={
    'filme': 'matrix',
    'ano':'1999',
    'diretor': 'wochowski'
}

locadora = [filme, filme_1, filme_2] #criando uma lista com dicionarios dentro. 
print(locadora)
#[{'filme': 'star wars', 'ano': '1977', 'diretor': 'george lucas'},
#  {'filme': 'avengers', 'ano': '2012', 'diretor': 'joss whedon'},
#  {'filme': 'matrix', 'ano': '1999', 'diretor': 'wochowski'}]
