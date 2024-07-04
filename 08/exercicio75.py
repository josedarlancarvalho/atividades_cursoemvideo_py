'''Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
'''
n = (int(input("digite o numero: ")),
 int(input("digite o numero: ")),
 int(input("digite o numero: ")),
 int(input("digite o numero: ")))
print(f"o nove apareceu {n.count(9)} vezes")
if 3 in n:
    print(f"o numero 3 apareceu na {n.index(3)+1} posicao.")  
else:
    print(f"o valor 3 nao foi digitado.")  
print(f"os valores pares digitados foram: ", end ='')
for a in n:
    if a % 2 == 0:
        print(a, end ='  ')
