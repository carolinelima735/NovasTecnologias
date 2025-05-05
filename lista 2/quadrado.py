#Quadrado oco de asteriscos

lado = int(input("Digite o tamanho do lado do quadrado (1 a 20): "))

if 1 <= lado <= 20:
    for i in range(lado):
        if i == 0 or i == lado - 1:
            print("*" * lado)
        else:
            print("*" + " " * (lado - 2) + "*")
else:
    print("Tamanho inválido!")
