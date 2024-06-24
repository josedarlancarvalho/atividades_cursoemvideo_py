#falando a primeira e ultima palavra da frase
nome = str(input("digite seu nome completo:")).strip()
n = nome.split()
print(n[0])
print((n[len(n)-1]))