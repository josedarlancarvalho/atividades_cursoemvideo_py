nome = str(input("digite seu nome completo: ")).strip()

print(f"seu nome em maiusculo é: {nome.upper()}")
print(f"seu nome em minusculo é: {nome.lower()}")
print(f"Seu nome ao todo tem {len(nome) - nome.count(" ")} letras") 
print(f"seu primeiro nome tem {nome.find(" ")}letras ")
