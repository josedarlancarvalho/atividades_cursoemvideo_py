#sabendo onde fica os A na frase
frase = str(input("digite a frase:")).strip().upper()
quantidade = frase.count("A")
primeira_vez = frase.find("A")
ultima_vez = frase.rfind("A")

print(f"A letra A apararece {quantidade} vezes na frase.")
print(f"A primeira letra A aparece na posicao:{primeira_vez}")
print(f"A letra A aparece pela ultima vez na posicao: {ultima_vez}")