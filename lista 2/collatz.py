n = int(input("Digite um número inteiro positivo: "))
passos = 0

while n != 1:
    print(n, end=" → ")
    if n % 2 == 0:
        n //= 2
    else:
        n = 3 * n + 1
    passos += 1

print("1")
print(f"Número de passos: {passos}")
