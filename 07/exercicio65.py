seguir = 'S'
media_cont = 0
media = 0
media_final = 0
maior = menor = 0
while seguir in 'Ss':
    num = int(input("digite um numero"))
    media += num
    media_cont += 1
    if media_cont == 1:
        maior = menor = num
    else:
        if num > maior: 
            maior = num
        if num < menor:
            menor = num
    seguir = str(input("quer continuar? [S/N]")).strip()[0].upper()
media_final = media / media_cont
print(f"maior numero digitado: {maior}")
print(f"menor numero digitado: {menor}")
print(f"quantidade de numeros digitados: {media_cont}")
print(f"media: {media_final}")
