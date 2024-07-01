num_1 = int(input("qual o valor do primeiro numero?"))
num_2 = int(input("qual o valor do segundo numero?"))
n = False
while not n:
    num_opcao = int(input("""Escolha uma das opcoes:
                             [ 1 ] somar
                             [ 2 ] multiplicar
                             [ 3 ] maior
                             [ 4 ] novos números
                             [ 5 ] sair do programa: """))
    if num_opcao == 1:
        num_resultado = num_1 + num_2
        print(f"a soma dos dois numeros é:{num_resultado}")
    elif num_opcao == 2:
        num_resultado = num_1 * num_2
        print(f"a multiplicacao dos dois numeros é:{num_resultado}")
    elif num_opcao == 3:
        if num_1 > num_2:
            print(f"o maior dos dois numeros é:{num_1}")
        else:
            print(f"o maior dos dois numeros é:{num_2}")
    elif num_opcao == 4:
        print("digite os novos valores.")
        num_1 = int(input("qual o valor do primeiro numero?"))
        num_2 = int(input("qual o valor do segundo numero?"))
    elif num_opcao == 5:
        break
    else:
       print ("opcao invalida. tente outra vez.")
    
    
