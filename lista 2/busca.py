#Busca linear em lista de palavras

lista = input("Digite palavras separadas por espaço: ").split()
termo = input("Digite a palavra que deseja buscar: ")

encontrou = False
for i in range(len(lista)):
    if lista[i] == termo:
        print(f"A palavra está no índice {i}")
        encontrou = True
        break

if not encontrou:
    print("Palavra não encontrada.")
