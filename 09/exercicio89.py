'''Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo 
em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário 
possa mostrar as notas de cada aluno individualmente.'''
nota = []
while True:
    teste = []
    nome = str(input("Qual o nome do aluno? "))
    teste.append(nome)
    nota_1 = float(input("Qual a nota 1? "))
    teste.append(nota_1)
    nota_2 = float(input("Qual a nota 2? "))
    teste.append(nota_2)
    media = (nota_1 + nota_2) / 2
    teste.append(media)
    nota.append(teste[:])   
    continuar = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if continuar == 'N':
        break
print("\nBoletim:")
print("No.   Nome       Média")
print("-----------------------")
for i, a in enumerate(nota):
    print(f"{i+1:<4}  {a[0]:<10}  {a[3]:<.2f}")
while True:
    opcao = int(input("\nQuer ver mais detalhes de quem? (999 para parar): "))
    if opcao == 999:
        break
    if 0 < opcao <= len(nota):
        aluno = nota[opcao - 1]
        print(f"Notas de {aluno[0]} são {aluno[1]}, {aluno[2]}")
    else:
        print("Opção inválida. Tente novamente.")
print("Fim")
