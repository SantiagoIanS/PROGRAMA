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

while len(maobot) < 2:
    m =random.choice(cartastodas)
    if m not in maobot:
        maobot.append(m)
    cartastodas.remove(m)

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
fichasbot = fichasuser - aposta1

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
fichasbot = fichasuser - aposta2
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

aposta3 = int(input("Quantas fichas você apostará na terceira rodada? (Escreva 0 para desistir) "))
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
maopokerbot = []
maopokerbot = maopokerbot + maomesa
maopokerbot = maopokerbot + maobot
maopokerbot.sort(key=lambda carta: valores_cartas_naipes[carta])
print(f", ".join(maopoker))
print(f", ".join(maopokerbot))

#Funções

#Valor das cartas
def valor_da_carta(carta):
    partes = carta.split()       # "10 ♠" → ["10", "♠"]
    valor = partes[0]            # Pega só "10"
    return valores_cartas[valor] # Usa o dicionário corretamente

pontosuser = 0
pontosbot = 0
#Royal Straight Flush        

#Straight Flush


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

#Carta Alta
def CartaAlta(mao):
    return not (
        Par(mao) or Doispares(mao) or Trinca(mao) or 
        Straight(mao) or Flush(mao) or FullHouse(mao) or 
        Quadra(mao)
    )

#mões
#USER
#Royal Straight Flush
if Straight(maopoker) == True and Flush(maopoker) == True and min(maopoker) == 10:
    pontosuser = 10
    print("Sua mão é um ROYAL STRAIGHT FLUSH!!!!!!")

#Straight Flush
elif Straight(maopoker) == True and Flush(maopoker) == True:
    pontosuser = 9
    print("Sua mão é um STRAIGHT FLUSH!!!!")

#Quadra
elif Quadra(maopoker) == True:
    pontosuser = 8
    print("Sua mão é uma QUADRA!!!")

#Full House
elif FullHouse(maopoker) == True:
    pontosuser = 7
    print("Sua mão é um FULL HOUSE!!")

#Flush
elif Flush(maopoker) == True:
    pontosuser = 6
    print("Sua mão é um FLUSH!")

#Straight
elif Straight(maopoker) == True:
    pontosuser = 5
    print("Sua mão é um STRAIGHT!")

#Trinca
elif Trinca(maopoker) == True:
    pontosuser = 4
    print("Sua mão é um Trinca")

#Dois pares
elif Doispares(maopoker) == True:
    pontosuser = 3
    print("Sua mão é um PARES")

#Par
elif Par(maopoker) == True:
    pontosuser = 2
    print("Sua mão é um PAR")

#Carta Alta
elif CartaAlta(maopoker) == True:
    pontosuser = 1
    print("Sua mão é uma CARTA ALTA")


#BOT
#Royal Straight Flush
if Straight == True and Flush == True and min == 10:
    pontosbot = 10
    print("A mão do bot é um ROYAL STRAIGHT FLUSH!!!!!!")

#Straight Flush
elif Straight(maopokerbot) == True and Flush(maopokerbot) == True:
    pontosbot = 9
    print("A mão do bot é um STRAIGHT FLUSH!!!!")

#Quadra
elif Quadra(maopokerbot) == True:
    pontosbot = 8
    print("A mão do bot é uma QUADRA!!!")

#Full House
elif FullHouse(maopokerbot) == True:
    pontosbot = 7
    print("A mão do bot é um FULL HOUSE!!")

#Flush
elif Flush(maopokerbot) == True:
    pontosbot = 6
    print("A mão do bot é um FLUSH!")

#Straight
elif Straight(maopokerbot) == True:
    pontosbot = 5
    print("A mão do bot é um STRAIGHT!")

#Trinca
elif Trinca(maopokerbot) == True:
    pontosbot = 4
    print("A mão do bot é um Trinca")

#Dois pares
elif Doispares(maopokerbot) == True:
    pontosbot = 3
    print("A mão do bot é um DOIS PARES")

#Par
elif Par(maopokerbot) == True:
    pontosbot = 2
    print("A mão do bot é um PAR")

#Carta Alta
elif CartaAlta(maopokerbot) == True:
    pontosbot = 1
    print("A mão do bot é uma CARTA ALTA")

if pontosuser > pontosbot:
    print("VOCE GANHOU!!!!!!")
elif pontosuser == pontosbot:
    print("EMPATE")
else:
    print("PERDEU OTARIO")