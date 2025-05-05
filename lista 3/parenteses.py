expressao = input("Digite os parenteses: ")

pilha = []

for i in range(0,len(expressao)):
    if expressao[i]=='(':
        pilha.append(')')
    else:
        if len(pilha)==0:
            print("Expressao errada")
            pilha.append('x')
            break
        else:
            pilha.pop()

if len(pilha)==0:
    print("Expressao correta")