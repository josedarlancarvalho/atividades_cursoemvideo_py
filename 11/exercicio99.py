'''Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. 
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''
def maior( * num):
    cont = maior1 = 0
    print(f"\n analisando valores...")
    for valor in num:
        print(f"{valor}", end= '')
        if cont == 0:
            maior1 = valor
        else:    
            if valor > maior1:
                maior1 = valor
        cont +=1
    print(f"\n ao todo tiveram {cont} numeros")        
    print(f"maior numero foi: {maior1}")

maior(5, 2, 1, 4 )
#maior(3, 4, 8, 2 )
#maior(1, 6, 7, 4 )
#maior(3, 2, 4)