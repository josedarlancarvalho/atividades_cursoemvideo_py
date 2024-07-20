def leiaInt(num):
    while True:
        try:
            n = int(input(num))
        except (TypeError, ValueError):
            print("por favor, digite um numero inteiro:")
            continue
        except (KeyboardInterrupt):
            print("usuario parou.")
            break
        else:
            return n

def leiaFloat(num):
    while True:
        try:
            n = float(input(num))
        except (TypeError, ValueError):
            print("por favor, digite um numero valido real:")
            continue
        except (KeyboardInterrupt):
            print("usuario parou.")
            break
        else:
            return n
num = leiaInt('digite o valor inteiro: ')
num2 = leiaFloat('digite um real: ')
print(f"valor inteiro digitado: {num} e o valor real digitado: {num2}")

