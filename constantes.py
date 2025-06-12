# Constantes em Python

# Em Python, não existe uma palavra-chave específica para criar constantes (como 'const' em outras linguagens).
# Mas por convenção, usamos letras MAIÚSCULAS para indicar que uma variável é uma constante
# Ou seja, seu valor NÃO deve ser alterado depois de definido.

# Exemplos de constantes:

PI = 3.14159              # Valor aproximado de π (pi), usado em cálculos matemáticos
GRAVIDADE = 9.8           # Aceleração da gravidade na Terra (m/s²)
VELOCIDADE_DA_LUZ = 299792458  # Velocidade da luz no vácuo (m/s)
NOME_DA_EMPRESA = "Tech Solutions"  # Nome da empresa (exemplo fictício)

# Podemos usar essas constantes ao longo do código, sabendo que seus valores não mudarão:

def calcular_area_circulo(raio):
    """Calcula a área de um círculo usando a constante PI"""
    return PI * (raio ** 2)

# Exemplo de uso:
raio = 5
area = calcular_area_circulo(raio)
print("Área do círculo com raio", raio, "é:", area)

# Lembre-se: mesmo sendo uma constante, Python permite que você mude o valor.
# Mas isso NÃO é recomendado. Exemplo errado:
PI = 3  # ERRADO! Não devemos alterar o valor de uma constante.
