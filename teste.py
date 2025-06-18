valores_cartas = {"2":2, "10":10, "J":11, "Ás":14}

def valor_da_carta(carta):
    partes = carta.replace('\xa0', ' ').split()
    print(partes)  # <- vamos ver o que aparece aqui
    return valores_cartas.get(partes[0], 0)

print(valor_da_carta("10 ♠"))
print(valor_da_carta("J ♥"))
print(valor_da_carta("Ás ♦"))
