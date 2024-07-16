'''Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar 
o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. '''
def helper(com):
    help(com)
ajuda = ''
while True:
    ajuda = input("FUNCAO OU BIBLIOTECA? [FIM] PARA SAIR")
    if 'FIM' in ajuda.upper():
        break
    else:
        helper(ajuda)