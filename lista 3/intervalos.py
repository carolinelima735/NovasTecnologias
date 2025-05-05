def mesclar_intervalos(intervalos):
    if not intervalos:
        return []

    # Ordena os intervalos com base no início
    intervalos.sort(key=lambda x: x[0])
    intervalos_mesclados = [intervalos[0]]

    for inicio, fim in intervalos[1:]:
        ultimo_inicio, ultimo_fim = intervalos_mesclados[-1]
        if inicio <= ultimo_fim:
            intervalos_mesclados[-1] = (ultimo_inicio, max(ultimo_fim, fim))
        else:
            intervalos_mesclados.append((inicio, fim))
    return intervalos_mesclados

intervalos = [(1, 4), (2, 5), (7, 9), (8, 10), (12, 15), (14, 20)]
resultado = mesclar_intervalos(intervalos)
print("Intervalos mesclados:", resultado)