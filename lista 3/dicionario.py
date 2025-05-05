palavras = input("Digite as palavras separadas por espaço: ").split()

tamanhos = {palavra: len(palavra) for palavra in palavras}

print("Dicionário com a quantidade de letras de cada palavra:")
print(tamanhos)
