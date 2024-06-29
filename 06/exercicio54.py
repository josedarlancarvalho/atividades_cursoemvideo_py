from datetime import date
atual = date.today().year
maior_total = 0
menor_total = 0
for c in range(1, 7+1):
    ano = int(input(f"Ano da {c} pessoa:"))
    idade = atual - ano
    if idade >= 18:
        maior_total += 1
    else:
        menor_total += 1
print(f"tivemos {maior_total} maiores de idade")
print(f"e tivemos {menor_total} menores de idade.")