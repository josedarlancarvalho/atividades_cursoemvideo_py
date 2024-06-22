import random
aluno_1 = str(input("digite o nome do primeiro aluno"))
aluno_2 = str(input("digite o nome do segundo aluno"))
aluno_3 = str(input("digite o nome do terceiro aluno"))
aluno_4 = str(input("digite o nome do quarto aluno"))

alunos = [aluno_1, aluno_2, aluno_3, aluno_4]

sorteado = random.choice(alunos)

print(f"o sorteador foi {sorteado}.")

#sorteia um