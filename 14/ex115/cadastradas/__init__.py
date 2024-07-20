from ex115.cadastrar import cadastradas

def ver_cadastradas():
    print("---------------------")
    print("-----Cadastradas-----")
    print("---------------------")
    if not cadastradas:
        print("Nenhuma pessoa cadastrada.")
    else:
        for pessoa in cadastradas:
            print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}")
    print("---------------------")