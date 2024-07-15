# Resumo sobre Funções em Python

# Definindo uma função simples
def saudacao():
    # Função que imprime uma saudação
    print("Olá, mundo!")

# Chamando a função saudacao
saudacao()
# Saída: Olá, mundo!

# Função com parâmetros
def saudacao_personalizada(nome):
    # Função que imprime uma saudação personalizada com o nome fornecido
    print(f"Olá, {nome}!")

# Chamando a função saudacao_personalizada com o argumento "Alice"
saudacao_personalizada("Alice")
# Saída: Olá, Alice!

# Função com retorno
def soma(a, b):
    # Função que retorna a soma de dois números
    return a + b

# Chamando a função soma com os argumentos 3 e 5
resultado = soma(3, 5)
print(resultado)
# Saída: 8

# Função com parâmetros opcionais
def saudacao_opcional(nome="visitante"):
    # Função que imprime uma saudação personalizada com um parâmetro opcional
    print(f"Olá, {nome}!")

# Chamando a função saudacao_opcional sem argumento
saudacao_opcional()
# Saída: Olá, visitante!

# Chamando a função saudacao_opcional com o argumento "Carlos"
saudacao_opcional("Carlos")
# Saída: Olá, Carlos!

# Função com vários parâmetros
def somar(*numeros):
    # Função que retorna a soma de vários números
    total = 0
    for numero in numeros:
        total += numero
    return total

# Chamando a função somar com vários argumentos
print(somar(1, 2, 3, 4, 5))
# Saída: 15

# Função com parâmetros nomeados
def dados_pessoais(nome, idade, cidade):
    # Função que imprime dados pessoais formatados
    print(f"Nome: {nome}, Idade: {idade}, Cidade: {cidade}")

# Chamando a função dados_pessoais com argumentos nomeados
dados_pessoais(nome="Maria", idade=30, cidade="São Paulo")
# Saída: Nome: Maria, Idade: 30, Cidade: São Paulo

# Função que retorna múltiplos valores
def operacoes(a, b):
    # Função que retorna a soma e a subtração de dois números
    soma = a + b
    subtracao = a - b
    return soma, subtracao

# Chamando a função operacoes e desempacotando os valores retornados
s, sub = operacoes(10, 5)
print(f"Soma: {s}, Subtração: {sub}")
# Saída: Soma: 15, Subtração: 5

# Função lambda
dobro = lambda x: x * 2  # Definindo uma função lambda que retorna o dobro de um número

# Chamando a função lambda
print(dobro(5))
# Saída: 10

# Função dentro de função
def calcular(op):
    # Função que retorna uma função que realiza uma operação matemática
    def soma(a, b):
        return a + b

    def subtracao(a, b):
        return a - b

    if op == "soma":
        return soma
    elif op == "subtracao":
        return subtracao

# Obtendo a função soma a partir da função calcular
operacao = calcular("soma")
print(operacao(10, 5))
# Saída: 15

# Obtendo a função subtracao a partir da função calcular
operacao = calcular("subtracao")
print(operacao(10, 5))
# Saída: 5

# Escopo de variáveis
def escopo_variavel():
    # Variável local definida dentro da função
    variavel_local = 10
    print(f"Variável local: {variavel_local}")

# Chamando a função escopo_variavel
escopo_variavel()
# Saída: Variável local: 10

# Variável global definida fora da função
variavel_global = 20

def escopo_variavel_global():
    # Acessando a variável global dentro da função
    global variavel_global
    variavel_global = 30
    print(f"Variável global: {variavel_global}")

# Chamando a função escopo_variavel_global
escopo_variavel_global()
# Saída: Variável global: 30
# O valor da variável global foi alterado para 30

print(f"Variável global fora da função: {variavel_global}")
# Saída: Variável global fora da função: 30
