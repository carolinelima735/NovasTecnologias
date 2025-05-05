from collections import Counter

# Entrada dos números separados por espaço
entrada = input("Digite os números separados por espaço: ")
numeros = list(map(int, entrada.split()))

# Entrada da frequência mínima
frequencia_minima = int(input("Digite a frequência mínima: "))

# Conta a frequência de cada número
contagem = Counter(numeros)

# Filtra apenas os números que aparecem pelo menos a frequência mínima
resultado = {numero: freq for numero, freq in contagem.items() if freq >= frequencia_minima}

# Exibe o resultado
print("\nNúmeros que aparecem pelo menos", frequencia_minima, "vezes:")
if resultado:
    for numero, freq in resultado.items():
        print(f"{numero}: {freq} vezes")
else:
    print("Nenhum número atinge a frequência mínima.")

