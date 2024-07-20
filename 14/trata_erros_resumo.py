# resumo_try_except.py

"""
Tratamento de Erros e Exceções em Python com try e except

Quando programamos, é comum que erros ocorram em tempo de execução, como dividir um número por zero ou acessar 
um índice inexistente em uma lista. Para lidar com esses erros de maneira elegante e evitar que o programa pare 
abruptamente, Python oferece a estrutura try e except.
"""

# Estrutura Básica
"""
A estrutura básica do try e except é a seguinte:
"""

try:
    # bloco de código que pode gerar um erro
    ...
except TipoDeErro:
    # bloco de código que será executado se ocorrer um erro do tipo especificado
    ...

# Funcionamento
"""
1. Bloco try:
   - Você coloca o código que pode potencialmente gerar um erro dentro do bloco try.
   - Se o código dentro do bloco try executa sem problemas, o bloco except é ignorado.
   - Se ocorre um erro dentro do bloco try, a execução do código é interrompida e Python procura um bloco except 
     correspondente ao tipo de erro.
     
2. Bloco except:
   - Você pode especificar o tipo de erro que deseja capturar. Por exemplo, ZeroDivisionError, ValueError, etc.
   - Se o tipo de erro corresponde ao especificado no except, o bloco de código dentro do except é executado.
   - Se você não especificar um tipo de erro, o except capturará todos os tipos de exceções.
"""

# Exemplo Básico
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")

# Capturando Múltiplos Tipos de Erros
try:
    resultado = int(input("Digite um número: "))
    print(f"O número digitado é {resultado}")
except ValueError:
    print("Erro: O valor digitado não é um número válido.")
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")

# else e finally
"""
- else: Você pode usar um bloco else após todos os blocos except. O código dentro do else será executado se nenhum 
  erro ocorrer no bloco try.
"""

try:
    resultado = int(input("Digite um número: "))
except ValueError:
    print("Erro: O valor digitado não é um número válido.")
else:
    print(f"O número digitado é {resultado}")

"""
- finally: O bloco finally será executado independentemente de ocorrer um erro ou não. É útil para limpar recursos, 
  como fechar arquivos ou conexões de rede.
"""

try:
    arquivo = open("dados.txt", "r")
    conteudo = arquivo.read()
except FileNotFoundError:
    print("Erro: Arquivo não encontrado.")
finally:
    arquivo.close()

# Dicas
"""
- Use try e except para tratar erros que você espera que possam ocorrer e que você sabe como lidar.
- Evite usar except sem especificar o tipo de erro, pois isso pode mascarar erros inesperados e dificultar a depuração.
"""

"""
Compreender e utilizar try e except permite que seu código seja mais robusto e resiliente a erros, proporcionando 
uma melhor experiência para o usuário.
"""

# Fim do resumo
