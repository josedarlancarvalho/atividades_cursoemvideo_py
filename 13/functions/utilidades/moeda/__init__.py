
def aumentar(num=0, format=False):
    aumento = num + (num * 0.10)
    return aumento if format is False else moedas(aumento)


def diminuir(num=0, format=False):
    diminui = num - (num * 0.10)
    return diminui if format is False else moedas(diminui)


def dobro(num=0, format=False):
    a = num * 2
    return a if format is False else moedas(a)


def metade(num=0, format=False):
    a = num / 2
    return a if format is False else moedas(a)


def moedas(num=0, moeda='R$'):
    if isinstance(num, (int, float)):
        return f'{moeda}{num:8.2f}'.replace('.', ',')
    else:
        return "Valor inválido"
    
def resumo_moeda(valor):
    print('-' * 30)
    print(f"Resumo do número: {moedas(valor)}")
    print(f"Dobro: {dobro(valor, True)}")
    print(f"Metade: {metade(valor, True)}")
    print(f"Aumento de 10%: {aumentar(valor, True)}")
    print(f"Desconto de 10%: {diminuir(valor, True)}")
    print('-' * 30)
