from ex115.cadastradas import ver_cadastradas
from ex115.cadastrar import cadastrar
from ex115.sair import sair

while True:
    print('''
    ESCOLHA UMA OPCAO:
    1- VER PESSOAS CADASTRADAS
    2- CADASTRAR PESSOA
    3- SAIR
    ''')
    try:
        opcao = int(input("escolha uma opcao: "))
    except (TypeError, ValueError):
        print("Opcao invalida. tente novamente.")
        continue
    except (KeyboardInterrupt):
        print("usuario parou")
        break
    if opcao == 1:
        ver_cadastradas()
    elif opcao == 2:
        cadastrar()
    elif opcao == 3:
        sair()
        break
    else:
        print("Opcao invalida. tente novamente.")
