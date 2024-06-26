num = int(input("Digite um numero: "))
print (f"""ESOLHA UMA OPCAO PARA CONVERTER (num)
       1 - Binario
       2- Octal
       3- Hexadecimal
       """) 
opcao = int(input("Escolha uma opcao"))
if opcao == 1:
    print(f"{num} em binario é {bin(num)[2:]}")
elif opcao == 2:
    print(f"{num} em octal é {oct(num)[2:]}")
elif opcao == 3:
    print(f"{num} em hexadecimal é {hex(num)[2:]}")
else:
    print("opcao invalide")
    