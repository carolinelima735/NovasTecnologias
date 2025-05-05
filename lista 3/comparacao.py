# Entrada das duas listas
lista1 = list(map(int, input("Digite os elementos da primeira lista (separados por espaço): ").split()))
lista2 = list(map(int, input("Digite os elementos da segunda lista (separados por espaço): ").split()))

# Conversão para conjuntos
conjunto1 = set(lista1)
conjunto2 = set(lista2)

# Operações com conjuntos
comuns = conjunto1 & conjunto2
so_primeira = conjunto1 - conjunto2
so_segunda = conjunto2 - conjunto1
nao_repetidos = conjunto1 ^ conjunto2
primeira_sem_repetidos = [num for num in lista1 if num not in conjunto2]

# Resultados
print("\nValores comuns às duas listas:", list(comuns))
print("Valores que só existem na primeira:", list(so_primeira))
print("Valores que existem apenas na segunda:", list(so_segunda))
print("Elementos não repetidos nas duas listas:", list(nao_repetidos))
print("Primeira lista sem os elementos repetidos na segunda:", primeira_sem_repetidos)
