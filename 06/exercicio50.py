soma= 0
for c in range(1,7):
    n = int(input("digite um numero:"))
    if n % 2 == 0:
        soma += n
print(f"soma de todos: {soma}")