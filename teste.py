valores_cartas = {"2":2, "10":10, "J":11, "Ás":14}
cartas = [10, 11, 12, 13, 14]

def valor_da_carta(carta):
    partes = carta.replace('\xa0', ' ').split()
    print(partes)  # <- vamos ver o que aparece aqui
    return valores_cartas.get(partes[0], 0)

print(valor_da_carta("10 ♠"))
print(valor_da_carta("J ♥"))
print(valor_da_carta("Ás ♦"))

def StraighFlushFoda(mao):
    naipes = [cartas.split()[1] for carta in mao]
    valores = [valor_da_carta(c) for c in mao]
    valores = list(set(valores))
    if 14 in valores:
        valores.append(1)

    valores.sort()
    for i in range(len(valores) - 4) and naipes in naipes:
        if naipes.count(naipes) >= 5 and valores[i+1] == valores[i] + 1 and \
            valores[i+2] == valores[i] + 2 and \
            valores[i+3] == valores[i] + 3 and \
            valores[i+4] == valores[i] + 4:
            return True
        return False
print(StraighFlushFoda(cartas))