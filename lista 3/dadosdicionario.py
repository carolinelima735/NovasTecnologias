# Lista para armazenar os dicionários de várias pessoas
pessoas = []

while True:
    print("\nDigite os dados da pessoa:")
    first_name = input("Primeiro nome: ")
    last_name = input("Sobrenome: ")
    age = input("Idade: ")
    city = input("Cidade onde vive: ")

    # Criando o dicionário para uma pessoa
    pessoa = {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "city": city
    }

    # Adiciona a pessoa à lista
    pessoas.append(pessoa)

    # Pergunta se deseja continuar
    continuar = input("Deseja adicionar outra pessoa? (s/n): ").lower()
    if continuar != 's':
        break

# Exibe todas as informações armazenadas
print("\n--- Informações das pessoas cadastradas ---")
for i, pessoa in enumerate(pessoas, 1):
    print(f"\nPessoa {i}:")
    print("Primeiro nome:", pessoa["first_name"])
    print("Sobrenome:", pessoa["last_name"])
    print("Idade:", pessoa["age"])
    print("Cidade:", pessoa["city"])
