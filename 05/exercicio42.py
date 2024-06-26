num_1 = int(input("digite o primeiro segmento"))
num_2 = int(input("digite o segundo segmento"))
num_3 = int(input("digite o terceiro segmento"))

if num_1 < num_2 + num_3 and num_2 < num_1 + num_3 and num_3 < num_1 + num_2:
    print("podem formar um tringulo", end ='')
    if num_1 == num_2 == num_3:
        print("equilatero")
    elif num_1 != num_2 != num_3 != num_1:
        print("escaleno")
    else:
        print("isosceles")
else:
    print("os segmentos nao podem formar um triangulo")