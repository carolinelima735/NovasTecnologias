msg = input("Digite a mensagem de 4 dígitos: ")
dig1 = (int(msg[0])+7)%10
dig2 = (int(msg[1])+7)%10
dig3 = (int(msg[2])+7)%10
dig4 = (int(msg[3])+7)%10

dig1,dig2,dig3,dig4 = dig3,dig4,dig1,dig2

print(f"Criptografada: {dig1}{dig2}{dig3}{dig4}")

dig1,dig2,dig3,dig4 = dig3,dig4,dig1,dig2

dig1 = (dig1+3)%10
dig2 = (dig2+3)%10
dig3 = (dig3+3)%10
dig4 = (dig4+3)%10

print(f"Descriptografada: {dig1}{dig2}{dig3}{dig4}")