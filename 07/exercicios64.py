num = cont = soma = 0 
num = int(input("digite um numero: "))
while num != 999:
    soma += num
    cont += 1
    num = int(input("digite um numero: "))
print(f"foram mostrados {cont} numeros")
print(f"soma dos numeros: {soma}")