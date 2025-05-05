#Somar todos os números pares entre 1 e N

N = int(input("Digite um número inteiro: "))
soma = 0

for i in range(2, N+1, 2):  # começa do 2, vai até N, pulando de 2 em 2
    soma += i

print(f"A soma dos números pares de 1 até {N} é {soma}")
