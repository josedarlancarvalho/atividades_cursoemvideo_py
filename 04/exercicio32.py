ano = int(input("digite o ano para saber se ele é bissexto ou nao"))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("bissexto")
else:
    print("nao é bissexto")