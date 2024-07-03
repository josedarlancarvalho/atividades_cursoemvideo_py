'''Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. 
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''
mais_18 = qnt_homem = mulher_20 = 0
while True:
    cadastro_idade = int(input("Qual a idade? "))
    cadastro_sexo = str(input("Qual o Sexo? [M/F] ")).upper().strip()[0]
    if cadastro_sexo in "F":
        if cadastro_idade > 18:
            mais_18 +=1
        if cadastro_idade < 20:
            mulher_20 += 1
    if cadastro_sexo in 'M':
        qnt_homem += 1
        if cadastro_idade > 18:
            mais_18 +=1
    continuar = str(input("quer continuar?[S/N] ")).upper().strip()[0]
    if continuar in 'N':
        break    

print(f"{mais_18} tem mais de 18 anos.")
print(f"{qnt_homem} homens foram cadastrados. ")
print(f"{mulher_20} mulheres tem menos de 20 anos.")    
            
            
            
            
            
 