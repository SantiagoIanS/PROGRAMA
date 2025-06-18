import random
from collections import Counter


cartas = [[["Ás ♠", "2 ♠", "3 ♠", "4 ♠", "5 ♠", "6 ♠", "7 ♠", "8 ♠", "9 ♠", "10 ♠", "J ♠", "Q ♠", "K ♠"], ["Ás ♣", "2 ♣", "3 ♣", "4 ♣", "5 ♣", "6 ♣", "7 ♣", "8 ♣", "9 ♣", "10 ♣", "J ♣", "Q ♣", "K ♣"], ["Ás ♥", "2 ♥", "3 ♥", "4 ♥", "5 ♥", "6 ♥", "7 ♥", "8 ♥", "9 ♥", "10 ♥", "J ♥", "Q ♥", "K ♥"], ["Ás ♦", "2 ♦", "3 ♦", "4 ♦", "5 ♦", "6 ♦", "7 ♦", "8 ♦", "9 ♦", "10 ♦", "J ♦", "Q ♦", "K ♦"]]]
cartastodas = ["Ás ♠", "2 ♠", "3 ♠", "4 ♠", "5 ♠", "6 ♠", "7 ♠", "8 ♠", "9 ♠", "10 ♠", "J ♠", "Q ♠", "K ♠", "Ás ♣", "2 ♣", "3 ♣", "4 ♣", "5 ♣", "6 ♣", "7 ♣", "8 ♣", "9 ♣", "10 ♣", "J ♣", "Q ♣", "K ♣", "Ás ♥", "2 ♥", "3 ♥", "4 ♥", "5 ♥", "6 ♥", "7 ♥", "8 ♥", "9 ♥", "10 ♥", "J ♥", "Q ♥", "K ♥", "Ás ♦", "2 ♦", "3 ♦", "4 ♦", "5 ♦", "6 ♦", "7 ♦", "8 ♦", "9 ♦", "10 ♦", "J ♦", "Q ♦", "K ♦"]
maomesa = []
fichasuser = 150
maouser = []
fichasbot = 150
maobot = []
valores_cartas_naipes = {"Ás ♠": 14, "2 ♠": 2, "3 ♠": 3, "4 ♠": 4, "5 ♠": 5, "6 ♠": 6, "7 ♠": 7, "8 ♠": 8, "9 ♠": 9, "10 ♠": 10, "J ♠": 11, "Q ♠": 12, "K ♠": 13, "Ás ♣": 14, "2 ♣": 2, "3 ♣": 3, "4 ♣": 4, "5 ♣": 5, "6 ♣": 6, "7 ♣": 7, "8 ♣": 8, "9 ♣": 9, "10 ♣": 10, "J ♣": 11, "Q ♣": 12, "K ♣": 13, "Ás ♥": 14, "2 ♥": 2, "3 ♥": 3, "4 ♥": 4, "5 ♥": 5, "6 ♥": 6, "7 ♥": 7, "8 ♥": 8, "9 ♥": 9, "10 ♥": 10, "J ♥": 11, "Q ♥": 12, "K ♥": 13, "Ás ♦": 14, "2 ♦": 2, "3 ♦": 3, "4 ♦": 4, "5 ♦": 5, "6 ♦": 6, "7 ♦": 7, "8 ♦": 8, "9 ♦": 9, "10 ♦": 10, "J ♦": 11, "Q ♦": 12, "K ♦": 13}
valores_cartas = {"Ás": 14, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13}
espadas = cartas[0][0]
paus = cartas[0][1]
copas = cartas[0][2]
ouros = cartas[0][3]

while len(maomesa) < 3:
    n = random.choice(cartastodas)
    if n not in maomesa:
        maomesa.append(n)
    cartastodas.remove(n)

while len(maouser) < 2:
    n =random.choice(cartastodas)
    if n not in maouser:
        maouser.append(n)
    cartastodas.remove(n)

#Por enquanto n vai ter bot
#while len(maobot) < 5:
#    n =random.choice(cartas)
#    if n not in maobot:
#        maobot.append(n)
#    cartas.remove(n)

print(f"----PRIMEIRAS RODADA----")
print("(", end="")
print(", ".join(maomesa), end="")
print(")")
print(" ")
print(f"Sua mão: ", end="")
print(", ".join(maouser))
print(f"Seu total de fichas são: {fichasuser}")

aposta1 = int(input("Quantas fichas você apostará na primeira rodada? (Escreva 0 para desistir) "))
if aposta1 == 0:
    print("Você desistiu")
    quit()
fichasuser = fichasuser - aposta1

print(f"Seu total de fichas atuais são: {fichasuser}")
print(f"Fichas na mesa: {aposta1}")
segundarodada = ""

n = random.choice(cartastodas)
if n not in segundarodada:
    segundarodada = n
cartastodas.remove(n)

maomesa.append(segundarodada)
print("")
print(f"----SEGUNDA RODADA----")
print(maomesa)
print(" ")
print(f"Sua mão: ", end="")
print(", ".join(maouser))
print(f"Seu total de fichas são: {fichasuser}")

aposta2 = int(input("Quantas fichas você apostará na segunda rodada? (Escreva 0 para desistir) "))
if aposta2 == 0:
    print("Você desistiu")
    quit()
fichasuser = fichasuser - aposta2
aposta = aposta1 + aposta2

print(f"Seu total de fichas atuais são: {fichasuser}")
print(f"Fichas na mesa: {aposta}")
print("")

terceirarodada = ""

n = random.choice(cartastodas)
if n not in terceirarodada:
    terceirarodada = n
cartastodas.remove(n)

maomesa.append(terceirarodada)
print(f"----TERCEIRA RODADA----")
print(maomesa)
print(" ")
print(f"Sua mão: ", end="")
print(", ".join(maouser))
print(f"Seu total de fichas são: {fichasuser}")

aposta3 = int(input("Quantas fichas você apostará na segunda rodada? (Escreva 0 para desistir) "))
if aposta3 == 0:
    print("Você desistiu")
    quit()
fichasuser = fichasuser - aposta3
aposta = aposta + aposta3

print(f"Seu total de fichas atuais são: {fichasuser}")
print(f"Fichas na mesa: {aposta}")
maopoker = []
maopoker = maopoker + maomesa
maopoker = maopoker + maouser
maopoker.sort(key=lambda carta: valores_cartas_naipes[carta])
print(f", ".join(maopoker))

#Funções

#Valor das cartas
def valor_da_carta(carta):
    partes = carta.split()       # "10 ♠" → ["10", "♠"]
    valor = partes[0]            # Pega só "10"
    return valores_cartas[valor] # Usa o dicionário corretamente



#Flush (Todos os naipes iguais)

def Flush(mao):
    naipes = [carta.split()[1] for carta in mao]  # pega só os naipes
    for naipe in naipes:
        if naipes.count(naipe) >= 5:
            return True
    return False

#Sequencia
def Straight(mao):
    # Converte a mão de strings para inteiros (valores)
    valores = [valor_da_carta(c) for c in mao]
    valores = list(set(valores))  # remove duplicatas

    # Se tiver Ás, considera também como 1 (para sequência A-2-3-4-5)
    if 14 in valores:
        valores.append(1)

    valores.sort()

    # Procura por 5 números consecutivos
    for i in range(len(valores) - 4):
        if valores[i+1] == valores[i] + 1 and \
           valores[i+2] == valores[i] + 2 and \
           valores[i+3] == valores[i] + 3 and \
           valores[i+4] == valores[i] + 4:
            return True
    return False

#Full House
def FullHouse(mao):
    valores = [carta.split()[0] for carta in mao]
    contagem = Counter(valores)
    trinca = False
    par = False
    for valor, qtd in contagem.items():
        if qtd >= 3:
            trinca = True  # encontrou uma trinca
        elif qtd >= 2:
            par = True
    return trinca and par

#Quadra
def Quadra(mao):
    valores = [carta.split()[0] for carta in mao]
    contagem = Counter(valores)
    for valor, qtd1 in contagem.items():
        if qtd1 == 4:
            return True  # encontrou um par
    return False

#Trinca
def Trinca(mao):
    valores = [carta.split()[0] for carta in mao]
    contagem = Counter(valores)
    for valor, qtd in contagem.items():
        if qtd == 3:
            return True  # encontrou um par
    return False

#Dois Pares
def Doispares(mao):
    valores = [carta.split()[0] for carta in mao]
    contagem = Counter(valores)
    pares = 0
    for qtd in contagem.values():
        if qtd >= 2:
            pares += 1

    return pares >= 2

#par
def Par(mao):
    valores = [carta.split()[0] for carta in mao]
    contagem = Counter(valores)
    for valor, qtd in contagem.items():
        if qtd == 2:
            return True  # encontrou um par
    return False

#mões
#Royal Straight Flush
if Straight(maopoker) == True and Flush(maopoker) == True and min(maopoker) == 10:
    print("Sua mão é um ROYAL STRAIGHT FLUSH!!!!!!")

#Straight Flush
elif Straight(maopoker) == True and Flush(maopoker) == True:
    print("Sua mão é um STRAIGHT FLUSH!!!!")

#Quadra
elif Quadra(maopoker) == True:
    print("Sua mão é uma QUADRA!!!")

#Full House
elif FullHouse(maopoker) == True:
    print("Sua mão é um FULL HOUSE!!")

#Flush
elif Flush(maopoker) == True:
    print("Sua mão é um FLUSH!")

#Straight
elif Straight(maopoker) == True:
    print("Sua mão é um STRAIGHT!")

#Trinca
elif Trinca(maopoker) == True:
    print("Sua mão é uma Trinca")

#Dois pares
elif Doispares(maopoker) == True:
    print("Sua mão é um DOIS PARES")

#Par
elif Par(maopoker) == True:
    print("Sua mão é um PAR")

#Carta Alta
else:
    print("Sua mão é uma CARTA ALTA")
