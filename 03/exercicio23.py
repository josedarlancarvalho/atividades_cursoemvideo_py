numero = int(input("digite um numero de 0 a 9999: "))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print (f"analisando o numero: {numero}")
print (f"unidade: {u}")
print (f"dezena: {d}")
print (f"centena: {c}")
print (f"milhar: {m}")
