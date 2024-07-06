'''Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.Depois disso, mostre:                                                                                                                                                
A) Quantos números foram digitados.                                                                                                                   
B) A lista de valores, ordenada de forma decrescente.                                                                                          
C) Se o valor 5 foi digitado e está ou não na lista.'''
lista = []
while True:
    lista.append(int(input("digite um numero: ")))
    continuar = str(input("quer continuar? [S/N]")).strip()[0].upper()
    if 'N' in continuar:
        break
print(f"quantidade de numeros na lista: {len(lista)}")
lista.sort(reverse=True)
print(f"Lista em ordem decrescente: {lista}")
if 5 in lista:
    print("sim, tem o numero 5.")
else:
    print("nao tem o numero 5")


