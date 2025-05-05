# função que multiplique dois polinômios e retorne o polinômio resultante, também como dicionário.

p1 = {2: 3, 1: 2, 0: 1}

p2 = {1:1, 0:4}

resultado = {}

for exp1, coef1 in p1.items():
    for exp2, coef2 in p2.items():
        exp_result = exp1+exp2
        coef_result = coef1*coef2

        resultado[exp_result] = resultado.get(exp_result,0)+coef_result

for exp, coef in resultado.items():
    print(f"{coef}x^{exp}",end="")

    if exp == 0:
        print(" = 0", end="")
    else:
        print(" + ", end="")