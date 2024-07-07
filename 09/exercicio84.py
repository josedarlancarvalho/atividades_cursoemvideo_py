'''Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:                                                                                                    
A) Quantas pessoas foram cadastradas.                                                                                                               
B) Uma listagem com as pessoas mais pesadas.                                                                                                    
c) Uma listagem com as pessoas mais leves.'''
teste = []
pessoa = []
leves = pesados = 0
while True:
    teste.append (str(input("nome da pessoa: ")))
    teste.append (int(input("peso da pessoa: ")))
    if len(pessoa) == 0:
        leves = pesados = teste[1]
    else:
        if teste[1] > pesados:
            pesados = teste[1]
        if teste[1] > pesados:
            leves = teste[1]
    pessoa.append(teste[:])
    teste.clear()
    continuar = str(input("quer continuar? [S/N]")).upper().strip()[0]
    if 'N' in continuar:
        break
print(f"{len(pessoa)} pessoas cadastradas.")
print(f"maior peso:{pesados}Kg e foi de: ", end ='')
for p in pessoa:
    if p[1] == pesados:
        print(f"{p[0]}", end ='')
print(f"menor peso:{leves}Kg e foi de: ", end ='')
for p in pessoa:
    if p[1] == pesados:
        print(f"{p[0]}", end ='')
