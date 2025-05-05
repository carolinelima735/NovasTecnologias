import string

texto = input("Digite uma palavra ou frase: ").lower()
# remover espaços e pontuações
texto_limpo = "".join(c for c in texto if c.isalnum())

if texto_limpo == texto_limpo[::-1]:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
