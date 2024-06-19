dia= int(input("ficou quantos dias com esse carro?"))
km = float(input("quantos km rodou?"))

valor_dia= dia * 60
valor_km = km * 15 / 100
valor_total = valor_dia + valor_km

print(f"o valor total a pagar é {valor_total}")