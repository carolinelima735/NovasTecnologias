palavras = ["amor", "roma", "mora", "carro", "orça", "orca", "arco"]

grupos={}

for palavra in palavras:
    chave = tuple(sorted(palavra.lower()))

    if chave in grupos:
        grupos[chave].append(palavra)
    else:
        grupos[chave]=[palavra]

for chave, grupo in grupos.items():
    print(f"{chave}:{grupo}")