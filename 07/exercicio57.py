s = str(input("digite o sexo: ")).strip().upper()[0]
while s not in 'MF':
    s = str(input("digite o sexo novamente: ")).strip().upper()[0]
print("ok")