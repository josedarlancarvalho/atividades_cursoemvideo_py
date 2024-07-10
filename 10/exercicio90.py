'''exercicio python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.'''
aluno = {}
aluno ['nome'] = str(input("nome do aluno: "))
aluno ['media'] = float(input("media do aluno: "))
if aluno['media'] >= 7:
    aluno['situacao'] = "aprovado"
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = "recuperacao"
else:
    aluno['situacao'] = 'reprovado'

for k, v in aluno.items():
    print(f"{k} = {v}")