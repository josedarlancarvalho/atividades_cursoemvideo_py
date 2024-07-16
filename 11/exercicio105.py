'''Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de
 alunos e vai retornar um dicionário com as seguintes informações:
– Quantidade de notas                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
– A maior nota                                                                                                                                                                
– A menor nota                                                                                                                                                              
– A média da turma                                                                                                                                                      
– A situação (opcional)'''
def notas(*num, sit=False):
    aluno = {}
    aluno['quantidade']= len(num)
    aluno['maior nota'] = max(num)
    aluno['menor nota'] = min(num)
    aluno['media']= sum(num)/len(num)
    if 'sit':
        if aluno['media'] >= 7:
            aluno['situacao'] = 'BOA'
        elif aluno['media'] >= 5:
            aluno['situacao'] = 'RAZOAVEL'
        else:
            aluno['situacao'] = 'RUIM'
    return aluno
resp = notas(1, 9, 0, 6, sit=True)    
print(resp)