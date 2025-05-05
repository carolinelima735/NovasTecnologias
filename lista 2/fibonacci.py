n = int(input("Digite a posição desejada (n ≥ 3): "))
a, b = 1, 1

for _ in range(n - 2):
    a, b = b, a + b

print(f"O {n}º termo da sequência de Fibonacci é: {b}")
