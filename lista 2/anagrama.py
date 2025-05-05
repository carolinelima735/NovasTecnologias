palavra1 = input("Digite a primeira palavra/frase: ").lower().replace(" ", "")
palavra2 = input("Digite a segunda palavra/frase: ").lower().replace(" ", "")

if sorted(palavra1) == sorted(palavra2):
    print("São anagramas!")
else:
    print("Não são anagramas.")
