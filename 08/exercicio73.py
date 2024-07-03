'''Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato 
Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''
time = ('corinthians', 'palmeiras', 'sao paulo', 'santos', 'chapecoense', 'flamengo', 'fluminense', 'botafogo', 'vasco', 'coritiba', 'athletico', 'nautico', 'santacruz', 'sport', 'cuiaba', 'gremio', 'internacional', 'bahia', 'vitoria', 'ibis')
print(time[:5])
print(time[-4:])
print(f"ordem alfabetica: {sorted(time)}")
print(time.index('chapecoense')+1)