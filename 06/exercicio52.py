num = int(input("digite um numero:"))
tot= 0
for c in range(1, num + 1):
    if num % c == 0:
        print(f"{c}")
        tot += 1
    else:
        print(f"{- c}")
if tot == 2:
    print(f"\n{num} é primo")
else:
    print(f"\n{num} nao é primo")