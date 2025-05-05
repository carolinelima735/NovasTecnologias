N = int(input("Digite um número inteiro: "))
primos = [True] * (N + 1)
primos[0] = primos[1] = False

for i in range(2, int(N**0.5) + 1):
    if primos[i]:
        for j in range(i*i, N+1, i):
            primos[j] = False

print("Números primos até", N, ":")
for i in range(N+1):
    if primos[i]:
        print(i, end=" ")
