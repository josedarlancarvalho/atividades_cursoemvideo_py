a = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    b = int(input("digite um numero: "))
    if b < 0 or b > 20:
        b = int(input("valor incorreto. digite um numero de 0 a 20: "))
    print(f'{a[b]}')
    break
