prim_ter = int(input("Primeiro termo:"))
razao= int(input("Razao:"))
decimo = prim_ter + (10 - 1) * razao
for c in range (prim_ter, decimo + razao, razao):
        print(c)