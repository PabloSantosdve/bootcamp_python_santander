# Conversão de tipos em Python (Type Casting)

# Às vezes precisamos converter um valor de um tipo para outro, por exemplo:
# de string para inteiro, de inteiro para float, etc.

# Python oferece funções para isso: int(), float(), str(), bool()

# Exemplos:

# Convertendo string para inteiro
numero_texto = "10"
numero_inteiro = int(numero_texto)  # Converte a string "10" para o número inteiro 10
print("Número inteiro:", numero_inteiro)

# Convertendo inteiro para float
numero_float = float(numero_inteiro)  # Converte 10 para 10.0
print("Número float:", numero_float)

# Convertendo número para string
numero_str = str(numero_float)  # Converte 10.0 para "10.0"
print("Número como string:", numero_str)

# Convertendo para booleano
valor1 = bool(0)      # False, pois 0 é considerado "falso"
valor2 = bool(100)    # True, qualquer número diferente de 0 é "verdadeiro"
valor3 = bool("")     # False, string vazia é "falsa"
valor4 = bool("Oi")   # True, string com conteúdo é "verdadeira"

print("bool(0):", valor1)
print("bool(100):", valor2)
print("bool(\"\"):", valor3)
print("bool(\"Oi\"):", valor4)

# Exemplo de uso prático: somar número digitado pelo usuário
entrada = "7"
resultado = int(entrada) + 3  # Convertendo a string para inteiro antes de somar
print("Resultado da soma:", resultado)
