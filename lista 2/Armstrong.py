inicio = int(input("Início do intervalo: "))
fim = int(input("Fim do intervalo: "))

for num in range(inicio, fim + 1):
    digitos = list(map(int, str(num)))
    soma = sum(d ** len(digitos) for d in digitos)
    if soma == num:
        print(num)
