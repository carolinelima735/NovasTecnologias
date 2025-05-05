import random

numero_secreto = random.randint(1, 100)
tentativa = 0

while True:
    tentativa += 1
    palpite = int(input("Adivinhe o número (entre 1 e 100): "))

    if palpite < numero_secreto:
        print("Muito baixo!")
    elif palpite > numero_secreto:
        print("Muito alto!")
    else:
        print(f"Parabéns! Você acertou em {tentativa} tentativas.")
        break
