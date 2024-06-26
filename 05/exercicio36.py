valor_casa = float(input("qual o valor da casa?"))
salario = float(input("qual o seu salario?"))
anos_parcela = int(input("em quantos anos pretende pagar a casa?"))

prestacao = valor_casa / (anos_parcela * 12)
minino = (salario * 30) / 100

if prestacao <= minino:
    print("pode financiar a casa.")
else:
    print("infelizmente voce nao pode fincanciar a casa. seu salario nao é compativel")