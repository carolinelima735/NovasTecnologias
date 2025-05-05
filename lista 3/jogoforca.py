import random

palavras = [
    "sol",         # 3 letras
    "lua",         # 3 letras
    "mar",         # 3 letras
    "estrela",     # 7 letras
    "cometa",      # 6 letras
    "planeta",     # 7 letras
    "galáxia",     # 7 letras
    "universo",    # 8 letras
    "satélite",    # 8 letras
    "cosmos",      # 6 letras
    "asteroide",   # 9 letras
    "espaço",      # 6 letras
    "viagem",      # 6 letras
    "órbita",      # 6 letras
    "cinturão"     # 8 letras
]

palavra=list(palavras[random.randint(0,len(palavras))])
resposta = ["_" for _ in palavra]
forca = ["""\\""","""\\O""","""\\O/""",
         """
         \\O/
           |""",
         """
         \\O/
           |
          /""", """
         \\O/
           |
          /\\"""]

while True:
    print()
    palpite = input("Digite uma letra: ")

    if palpite not in palavra:
        print(forca.pop(0))
        
    for i,letra in enumerate(palavra):
        if palpite==letra:
           resposta[i] = letra

    for letra  in resposta:
        print(letra, end="")

    if resposta==palavra:
        print()
        print("Acertou a palavra!")
        break
    elif len(forca)==0:
        print()
        print("Você perdeu!")
        break