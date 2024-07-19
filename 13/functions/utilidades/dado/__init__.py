def leiaDinheiro(msg):
    while True:
        entrada = input(msg).replace(',', '.').strip()
        if entrada.replace('.', '').isdigit():
            return float(entrada)
        else:
            print(f"ERRO: '{entrada}' é um preço inválido!")
