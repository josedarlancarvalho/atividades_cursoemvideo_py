media_grupo = 0
media_soma = 0
maior_idade = 0
nome_velho = ''
mulher_20 = 0

for c in range(1, 5):
    print(f"====={c}ª pessoa=====")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").strip().upper()
    
    media_soma += idade
    if c == 1 and sexo == 'M':
        maior_idade = idade
        nome_velho = nome
    if sexo == 'M' and idade > maior_idade:
        maior_idade = idade
        nome_velho = nome
    if sexo == 'F' and idade < 20:
        mulher_20 += 1

media_grupo = media_soma / 4

print(f"A média de idade do grupo é: {media_grupo}")
print(f"O homem mais velho é {nome_velho} com {maior_idade} anos")
print(f"Existem {mulher_20} mulher com menos de 20 anos")
