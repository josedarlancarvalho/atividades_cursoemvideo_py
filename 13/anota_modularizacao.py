# Modularização e Pacotes em Python

# A modularização é o processo de dividir um programa em partes menores e gerenciáveis, chamadas módulos.
# Pacotes são coleções de módulos organizados em diretórios.

# Criação de Módulos:
# Um módulo é simplesmente um arquivo Python que contém funções, classes e variáveis.
# Por exemplo, crie um arquivo chamado meu_modulo.py:
# meu_modulo.py
def saudacao(nome):
    return f"Olá, {nome}!"

# Utilização de Módulos:
# Você pode importar e utilizar módulos em outros arquivos Python usando a palavra-chave 'import'.
import meu_modulo

nome = "Darlan"
print(meu_modulo.saudacao(nome))  # Output: Olá, Darlan!

# Importando partes específicas de um módulo:
# Você pode importar funções ou classes específicas de um módulo.
from meu_modulo import saudacao

print(saudacao("Maria"))  # Output: Olá, Maria!

# Pacotes:
# Um pacote é um diretório que contém vários módulos e um arquivo __init__.py.
# Estrutura de diretório de exemplo:
# meu_pacote/
#   __init__.py
#   modulo1.py
#   modulo2.py

# Crie um arquivo __init__.py vazio para indicar que o diretório deve ser tratado como um pacote.
# O arquivo __init__.py pode também inicializar o pacote ou definir o que será exportado.

# __init__.py
# (Pode estar vazio ou pode conter código de inicialização do pacote)

# modulo1.py
def funcao_modulo1():
    return "Função do módulo 1"

# modulo2.py
def funcao_modulo2():
    return "Função do módulo 2"

# Importando módulos de um pacote:
# Você pode importar módulos de um pacote usando a sintaxe de ponto.
from meu_pacote import modulo1, modulo2

print(modulo1.funcao_modulo1())  # Output: Função do módulo 1
print(modulo2.funcao_modulo2())  # Output: Função do módulo 2

# Você também pode usar a sintaxe de ponto para importar partes específicas de um módulo.
from meu_pacote.modulo1 import funcao_modulo1

print(funcao_modulo1())  # Output: Função do módulo 1

# Importando pacotes:
# Se um pacote contiver muitos módulos, você pode importar o pacote inteiro e usar a notação de ponto para acessar seus módulos.
import meu_pacote

print(meu_pacote.modulo1.funcao_modulo1())  # Output: Função do módulo 1
print(meu_pacote.modulo2.funcao_modulo2())  # Output: Função do módulo 2

# Importando todos os itens de um módulo:
# Você pode importar todos os itens de um módulo usando '*', mas isso não é recomendado, pois pode causar conflitos de nomes.
from meu_modulo import *

print(saudacao("Carlos"))  # Output: Olá, Carlos!

# Boas práticas de modularização e pacotes:
# - Organize seu código em módulos e pacotes para melhorar a legibilidade e reutilização.
# - Use nomes significativos para seus módulos e pacotes.
# - Evite usar importações globais (from modulo import *) para prevenir conflitos de nomes.
# - Documente seus módulos e pacotes para que outros desenvolvedores entendam seu código.
